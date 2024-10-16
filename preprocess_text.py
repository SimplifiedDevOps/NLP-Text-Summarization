# Function to clean and preprocess the extracted text
def preprocess_text(text):
    # Replace newlines and carriage returns with spaces
    text = text.replace('\n', ' ').replace('\r', '').strip()

    # Additional cleaning can be added here if necessary
    # For example, removing special characters, page numbers, etc.
    return text

# Load the extracted text from the text file
with open("Data/extracted_medical_text.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Preprocess the extracted text
cleaned_text = preprocess_text(raw_text)

# Save the cleaned text to a file
with open("Data/cleaned_medical_text.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)

# Display the first 500 characters of the cleaned text
print(cleaned_text[:500])
