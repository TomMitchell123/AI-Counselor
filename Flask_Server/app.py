from flask import Flask
from Testing_Back_End.pdf_processing import pdf
from Testing_Back_End.query_processing import query
from flask import request
from flask_cors import CORS

import aiParse2

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/process_pdf")
def process_pdf():
    jsonOutput = pdf.test("placeholder.pdf")
    return jsonOutput

@app.route("/process_query")
def process_query():
    text_output = aiParse2.call_ai(request.headers.get('input'))
    
    if "SQL" in text_output:
        return {"output": "Sorry, this query did not work. Try again!"}

    if "degree" in request.headers.get('input'):
        text_output += " For degree requirements go to http://registrar.vt.edu/graduation-multi-brief/index1.html"

    elif "requirement" in request.headers.get('input'):
        text_output += " For degree requirements go to http://registrar.vt.edu/graduation-multi-brief/index1.html"
        
    print(text_output)

    return {"output":text_output}

@app.route("/upload_pdf", methods=['POST'])
def upload_pdf():
    file = request.files['file']
    file.save(f"./incoming_pdf/{file.filename}")
    
    return "hello"
    