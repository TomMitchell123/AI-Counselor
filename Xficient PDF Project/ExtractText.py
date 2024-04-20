import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        total_text = ''
        for page in pdf.pages:
            total_text += page.extract_text() + '\n'  # Extract text from each page
        return total_text

# Example usage
pdf_text = extract_text_from_pdf('University_Course_Catalog_Data_Extraction_and_Query_Challenge.pdf')
print(pdf_text)
