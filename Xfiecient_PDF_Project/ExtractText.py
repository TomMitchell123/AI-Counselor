import subprocess
import os

def extract_text_from_pdf(pdf_path):
    #proc = subprocess.Popen(["pdf2txt", pdf_path], stdout=subprocess.PIPE, shell=True)
    proc = os.popen(f"pdf2txt {pdf_path}").read()
    return proc


if __name__ == "__main__":
    # Example usage
    pdf_text = extract_text_from_pdf('vt.pdf')
    print(pdf_text)
