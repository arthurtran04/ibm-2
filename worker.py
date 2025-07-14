# Import necessary libraries
import os
import torch
import logging
from huggingface_hub import InferenceClient
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging to display debug messages
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Initialize device to use GPU if available, otherwise use CPU
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

# Initialize global variables
conversation_retrieval_chain = None
chat_history = []
embeddings = None
inference_client = None

# Define the model ID for the InferenceClient
MODEL_ID = "HuggingFaceTB/SmolLM3-3B"


# Initialize InferenceClient and embeddings
def init_llm():
    # Use global variables to store embeddings and inference client
    global embeddings, inference_client
    logger.info("Initializing InferenceClient and embeddings...")

    # InferenceClient requires a Hugging Face token
    if "HF_TOKEN" not in os.environ:
        logger.error("Hugging Face token (HF_TOKEN) not found in environment variables.")
        raise EnvironmentError("Please set the HF_TOKEN environment variable with your Hugging Face token.")
    
    # Initialize InferenceClient and embeddings
    inference_client = InferenceClient(
        token=os.environ["HF_TOKEN"]
    )
    embeddings = HuggingFaceInstructEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": DEVICE}
    )
    logger.debug("InferenceClient and embeddings initialized.")


# Process PDF document
def process_document(document_path):
    # Use global variable to store the conversation retrieval chain
    global conversation_retrieval_chain
    logger.info("Loading document from path: %s", document_path)

    # Check if the document exists
    if not os.path.exists(document_path):
        logger.error("Document not found at path: %s", document_path)
        raise FileNotFoundError(f"Document not found at path: {document_path}")
    
    # Load the document using PyPDFLoader
    loader = PyPDFLoader(document_path)
    documents = loader.load()
    logger.debug("Loaded %d document(s)", len(documents))

    # Split the document into text chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
    texts = text_splitter.split_documents(documents)
    logger.debug("Document split into %d text chunks", len(texts))

    # Create a vector store using Chroma
    db = Chroma.from_documents(texts, embedding=embeddings)
    logger.debug("Chroma vector store initialized.")

    # Create a retriever from the vector store and save retriever for future use
    conversation_retrieval_chain = db.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25})
    logger.info("Retriever created successfully.")


# Send prompt to InferenceClient and return the result
def process_prompt(prompt):
    # Use global variables for conversation retrieval chain and chat history
    global conversation_retrieval_chain
    global chat_history
    logger.info("Processing prompt: %s", prompt)

    # If there is a document, get context from retriever
    context = ""
    if conversation_retrieval_chain is not None:
        docs = conversation_retrieval_chain.get_relevant_documents(prompt)
        context = "\n".join([doc.page_content for doc in docs])

    # Build messages array with chat history
    messages = []
    
    # Add system message if there's document context
    if context:
        system_message = f"You are a helpful assistant. Use the following context from the document to answer questions:\n\n{context}\n\nAnswer based on the context provided and be helpful and accurate."
        messages.append({"role": "system", "content": system_message})
    
    # Add chat history to messages
    max_history_exchanges = 5  # limit the number to avoid exceeding the token limit
    recent_history = chat_history[-max_history_exchanges:] if len(chat_history) > max_history_exchanges else chat_history
    
    for user_msg, assistant_msg in recent_history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": assistant_msg})
    
    # Add current user prompt
    messages.append({"role": "user", "content": prompt})
    
    # Send messages to InferenceClient
    answer = inference_client.chat_completion(
        model=MODEL_ID,
        messages=messages,
        temperature=0.1,
        max_tokens=1000  # Add token limit to avoid long response
    )
    answer = answer.choices[0].message.content
    logger.debug("Model response: %s", answer)

    # Update chat history with the prompt and answer
    chat_history.append((prompt, answer))
    logger.debug("Chat history updated. Total exchanges: %d", len(chat_history))

    return answer


# Initialize the LLM and embeddings
init_llm()
logger.info("InferenceClient and embeddings initialization complete.")