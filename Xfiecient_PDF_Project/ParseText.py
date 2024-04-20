import re

def parse_courses(text):
    courses = []
    # Example regex pattern to find courses, adjust according to actual text format
    pattern = re.compile(r'(\w{2,4}\s\d{3})\s-\s(.*?)\s\((\d) credits?\)', re.DOTALL)
    matches = pattern.finditer(text)
    for match in matches:
        course_code, course_title, credit_hours = match.groups()
        courses.append({
            'code': course_code.strip(),
            'title': course_title.strip(),
            'credit_hours': int(credit_hours)
        })
    return courses

# Example usage
courses = parse_courses(pdf_text)
print(courses)
