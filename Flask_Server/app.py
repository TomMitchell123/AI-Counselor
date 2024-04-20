from flask import Flask
from Testing_Back_End.pdf_processing import pdf
from Testing_Back_End.query_processing import query
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/process_pdf")
def process_pdf():
    jsonOutput = pdf.test("placeholder.pdf")
    return jsonOutput

@app.route("/process_query")
def process_query():
    text_output = query.process_query(request.headers.get('input'))
    print(text_output)
    return {"output":text_output}