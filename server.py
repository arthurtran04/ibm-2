'''
This is the main server file for the PDF chatbot.
It is responsible for handling the requests from the frontend and processing the documents.
'''
# Importing the necessary libraries
import logging
import os
import tempfile
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import worker  # Import the worker module

# Initialize Flask app and CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.logger.setLevel(logging.ERROR)

# Define the route for the index page
@app.route('/', methods=['GET'])
def index():
    '''
    This function renders the index.html template.
    '''
    return render_template('index.html')  # Render the index.html template

# Define the route for processing messages
@app.route('/process-message', methods=['POST'])
def process_message_route():
    '''
    This function processes the user's message and returns the bot's response.
    '''
    user_message = request.json['userMessage']  # Extract the user's message from the request
    print('user_message', user_message)

    # Process the user's message using the worker module
    bot_response = worker.process_prompt(user_message)

    # Return the bot's response as JSON
    return jsonify({
        "botResponse": bot_response
    }), 200

# Define the route for processing documents
@app.route('/process-document', methods=['POST'])
def process_document_route():
    '''
    This function processes the uploaded document and returns the bot's response.
    '''
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({
            "botResponse": "It seems like the file was not uploaded correctly, can you try "
                           "again. If the problem persists, try using a different file"
        }), 400

    file = request.files['file']  # Extract the uploaded file from the request

    # Create a temporary file to avoid saving it in the project directory
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        file.save(temp.name)
        temp_path = temp.name
    
    try:
        # Process the document using the worker module with the temporary path
        worker.process_document(temp_path)
    finally:
        # Clean up the temporary file after processing
        os.remove(temp_path)

    # Return a success message as JSON
    return jsonify({
        "botResponse": "Thank you for providing your PDF document. I have analyzed it, "
                       "so now you can ask me any questions regarding it!"
    }), 200

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
