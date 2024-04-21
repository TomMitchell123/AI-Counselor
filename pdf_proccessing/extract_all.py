import fitz  # PyMuPDF
import json
from extract_courses import *
from extract_policies import *

pdf_path = 'pdfs/vt.pdf'

def extract_text_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    text_by_page = {}
    for page in doc:
        text_by_page[page.number] = page.get_text()
    doc.close()
    return text_by_page

def extract_text_by_line(pdf_path, output_file):
    doc = fitz.open(pdf_path)
    text_by_page = {}
    for page in doc:
        blocks = page.get_text("blocks")  # Extract text blocks
        sorted_blocks = sorted(blocks, key=lambda b: (b[1], b[0]))  # Sort blocks by their vertical, then horizontal position
        text_by_page[page.number] = "\n".join([block[4] for block in sorted_blocks])  # Combine text of sorted blocks
    doc.close()

    with open(output_file, 'w') as file:
        for _, text in text_by_page.items():
            for line in text.splitlines():
                if line.strip():  # Check if line is not empty
                    file.write(line + "\n")

def write_to_json(courses_info, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(courses_info, file, ensure_ascii=False, indent=4)

text_by_page = extract_text_by_page(pdf_path)
extract_text_by_line(pdf_path, 'textbyline.txt')

courses_info = extract_courses(text_by_page)
write_to_json(courses_info, "../Flask_Server/data/cdata.json")

academic_policies = extract_academic_policies("textbyline.txt")
write_to_json(academic_policies, "../Flask_Server/data/pdata.json")