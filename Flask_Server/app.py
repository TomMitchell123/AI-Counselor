# Import necessary modules from Flask, Flask-CORS, and local modules for processing
from flask import Flask, request
from flask_cors import CORS
import Flask_Server.backend.ai_parse as ai_parse

# Initialize Flask app and configure CORS
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/process_query")
def process_query():
    """
    Route to process a query. It uses the ai_parse module to process the input from request headers.
    Depending on the input, it appends additional information to the output or returns an error message.
    """
    text_output = ai_parse.call_ai(request.headers.get('input'))
    
    # Check for SQL in the output and return an error message if found
    if "SQL" in text_output:
        return {"output": "Sorry, this query did not work. Try again!"}

    # Append additional information based on specific keywords in the input
    if "degree" in request.headers.get('input'):
        text_output += " For degree requirements go to http://registrar.vt.edu/graduation-multi-brief/index1.html"
    elif "requirement" in request.headers.get('input'):
        text_output += " For degree requirements go to http://registrar.vt.edu/graduation-multi-brief/index1.html"
        
    # Log the final text output for debugging purposes
    print(text_output)

    return {"output":text_output}

@app.route("/upload_pdf", methods=['POST'])
def upload_pdf():
    """
    Route to upload a PDF file. It saves the uploaded file to a specified directory.
    """
    file = request.files['file']
    file.save(f"./incoming_pdf/{file.filename}")
    
    return "File uploaded successfully"
