import json

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
save_to_json(courses, 'extracted_courses.json')
