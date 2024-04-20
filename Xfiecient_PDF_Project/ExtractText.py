import fitz  # PyMuPDF

def extract_text_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    text_by_page = {}
    for page in doc:
        text_by_page[page.number] = page.get_text()
    doc.close()
    return text_by_page

pdf_path = 'vt.pdf'
text_by_page = extract_text_by_page(pdf_path)

# print(text_by_page)

import re

def find_course_info(course_code, text_by_page):
    # Regex that attempts to isolate a single course's description, stopping at the next course's code
    course_pattern = re.compile(rf"(\b{course_code}\b.+?)(?=\b[A-Z]+\s+\d+\.|\Z)", re.DOTALL)
    
    for page_number, text in text_by_page.items():
        match = course_pattern.search(text)
        if match:
            # Clean and return the first match only, to avoid capturing subsequent unrelated courses
            course_description = match.group(1).strip()
            # Post-process to split by lines and rejoin to avoid breaking phrases across lines
            course_description = ' '.join(course_description.split('\n'))
            return course_description, page_number
    return "Course not found", None

# Example usage:
course_code = "2404: INTRODUCTION TO APPLIED COLLABORATIVE TECHNIQUES"
course_info, page_number = find_course_info(course_code, text_by_page)
print(f"Course Info: {course_info}\nFound on page: {page_number}")