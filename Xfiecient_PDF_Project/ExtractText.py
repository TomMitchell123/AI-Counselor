import pdfplumber
import json
import re

data =	{}

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
            print("page down!")
    return text

def write_text_to_file(text, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    pdf_path = "vt.pdf"
    output_path = "output.txt"

    print(f"Extracting text from {pdf_path}...")

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_path)
    print("Finihsed extracting text!")

    # Write extracted text to a text file
    write_text_to_file(extracted_text, output_path)
    print(f"Text saved to {output_path}")

    pattern = r'(\d{4}): ([A-Z\s-]+)\n((?:.|\n)+?)(?=\n\d{4}|$)'
    # Find all matches in the input string
    matches = re.findall(pattern, extracted_text, re.DOTALL)

    # Print course information
    for match in matches:
        course_id = match[0]
        course_title = match[1]
        description = match[2].strip()

        matches = re.findall(r'\((.*?)\)', description)
        if matches:
            credits = matches[-1]  # Return the first match
        else:
            credits = "Variable"      

        # Adding data to the dictionary
        data[course_title] = {"ID": course_id, "Description": description, "Credits": credits}

        print("Adding data to the dictionary")

    # Writing data to JSON file
    with open('output.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
        print("Data saved to output.json")


