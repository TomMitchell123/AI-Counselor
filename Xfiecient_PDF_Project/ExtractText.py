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


import re
import json

def extract_courses(text_by_page):
    courses_list = []  # Changed from dict to list to accommodate the new structure
    # Adjusted regex to capture everything up to the start of the next course, including extracting credits explicitly
    course_pattern = re.compile(r"(\d{4}): ([^\n]+)\n(.*?)(\(\d+H,\d+C\))?(?=\d{4}:|\Z)", re.DOTALL)

    for page_number, text in text_by_page.items():
        for match in course_pattern.finditer(text):
            course_id = match.group(1).strip()
            course_title = match.group(2).strip()  # Keep course title as is, without converting to uppercase
            course_description = match.group(3).strip()

            # Remove the credits from the end of the description if they are included
                
            credits_search = re.search(r'\((\d+H,\d+C)\)$', course_description)
            
            if credits_search:
                course_credits = credits_search.group(1)  # Extract the credits information
                course_description = re.sub(r'\s*\(\d+H,\d+C\)$', '', course_description)  # Remove the credits from the description
            else:
                course_credits = "Variable"
            
            if course_title.isupper():  # Only add courses with titles in all caps
                courses_list.append({
                    "course_name": course_title,
                    "course_id": course_id,
                    "course_description": course_description.strip(),
                    "course_credits": course_credits  # Properly separated credits
                })
    
    return {"courses": courses_list}  # Wrap the list in a dict under the key "courses"


def write_courses_to_json(courses_info, filename='courses_data.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(courses_info, file, ensure_ascii=False, indent=4)

# Assuming text_by_page has been defined elsewhere
courses_info = extract_courses(text_by_page)
write_courses_to_json(courses_info)




