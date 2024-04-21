import fitz  # PyMuPDF
import re

def extract_text_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    text_by_page = {}
    for page in doc:
        text_by_page[page.number] = page.get_text()
    doc.close()
    return text_by_page

def generate_course_code_regex(sample_course_code):
    # Generate regex pattern for course codes with similar format
    course_code_pattern = re.compile(rf"(\b\d{{{len(sample_course_code)}}}\b.+?)(?=\b[A-Z]+\s+\d+\.|\Z)", re.DOTALL)
    return course_code_pattern

def find_all_course_info(course_code_pattern, text_by_page):
    course_info_list = []
    # Iterate through each page's text
    for page_number, text in text_by_page.items():
        # Search for all occurrences of the course code pattern
        matches = re.finditer(course_code_pattern, text)
        # Collect all matches on the current page
        for match in matches:
            course_description = match.group(1).strip()
            course_description = ' '.join(course_description.split('\n'))
            course_info_list.append((course_description, page_number))
    return course_info_list

if __name__ == "__main__":
    # Example usage:
    pdf_path = 'vt.pdf'
    text_by_page = extract_text_by_page(pdf_path)

    # Prompt user to input a sample course code
    sample_course_code = input("Enter a sample course code: ")

    # Generate regex pattern based on the sample course code format
    course_code_pattern = generate_course_code_regex(sample_course_code)

    # Find all course information
    all_course_info = find_all_course_info(course_code_pattern, text_by_page)

    # Print all course information found
    for index, (course_info, page_number) in enumerate(all_course_info, start=1):
        print(f"Course {index} Info: {course_info}\nFound on page: {page_number}\n")
