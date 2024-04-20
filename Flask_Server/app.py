from flask import Flask
from Testing_Back_End.pdf_processing import pdf
from Testing_Back_End.query_processing import query

app = Flask(__name__)

@app.route("/process_pdf")
def process_pdf():
    jsonOutput = pdf.test("no one cares")
    return jsonOutput

@app.route("/process_query")
def process_query():
    text_output = query.process_query()