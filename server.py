import logging
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import worker  # Import the worker module

# Initialize Flask app and CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.logger.setLevel(logging.ERROR)

# Define the upload folder
UPLOAD_FOLDER = 'files'

# Create the upload folder if it doesn't exist
def create_upload_folder():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
        print(f"Created upload folder: {UPLOAD_FOLDER}")

# Define the route for the index page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  # Render the index.html template

# Define the route for processing messages
@app.route('/process-message', methods=['POST'])
def process_message_route():
    user_message = request.json['userMessage']  # Extract the user's message from the request
    print('user_message', user_message)

    bot_response = worker.process_prompt(user_message)  # Process the user's message using the worker module

    # Return the bot's response as JSON
    return jsonify({
        "botResponse": bot_response
    }), 200

# Define the route for processing documents
@app.route('/process-document', methods=['POST'])
def process_document_route():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({
            "botResponse": "It seems like the file was not uploaded correctly, can you try "
                           "again. If the problem persists, try using a different file"
        }), 400

    file = request.files['file']  # Extract the uploaded file from the request

    # Create upload folder if it doesn't exist
    create_upload_folder()

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)  # Define the path where the file will be saved

    try:
        file.save(file_path)  # Save the file to the files folder
        print(f"File saved to: {file_path}")
        
        worker.process_document(file_path)  # Process the document using the worker module
        
        # Return a success message as JSON
        return jsonify({
            "botResponse": "Thank you for providing your PDF document. I have analyzed it, so now you can ask me any "
                           "questions regarding it!"
        }), 200
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        # Clean up the file if processing failed
        if os.path.exists(file_path):
            os.remove(file_path)
        
        return jsonify({
            "botResponse": "Sorry, there was an error processing your document. Please try again with a different file."
        }), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=False)