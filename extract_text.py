import PyPDF2

# Define the path to the PDF file
pdf_path = r"C:\Users\avard\OneDrive\Documents\SimplifiedDevOps\NLP-Text-Summarization\Data\Medical_book.pdf"

# Function to extract text from the PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()  # Extract text from each page
    return text

# Extract text from the provided medical book PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Save the extracted text to a text file
with open("Data/extracted_medical_text.txt", "w", encoding="utf-8") as f:
    f.write(pdf_text)

# Display the first 500 characters of extracted text to verify
print(pdf_text[:500])
