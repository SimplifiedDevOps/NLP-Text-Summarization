import re
import json

# Define regular expressions to identify sections
section_patterns = {
    'definition': r"Definition[:\s]+",
    'description': r"Description[:\s]+",
    'purpose': r"Purpose[:\s]+",
    'precautions': r"Precautions[:\s]+",
    'preparation': r"Preparation[:\s]+",
    'results': r"Results[:\s]+"
}

# Function to create pairs by splitting the text into sections and pairing description with different sections
def create_summarization_pairs(text):
    pairs = []

    # Split the text based on 'Definition' sections (as the beginning of each section)
    sections = re.split(section_patterns['definition'], text)

    for section in sections[1:]:  # Skip the first one as it's before the first 'Definition'
        # Find the next sections: Description, Purpose, Precautions, etc.
        description_match = re.search(section_patterns['description'], section)
        purpose_match = re.search(section_patterns['purpose'], section)
        precautions_match = re.search(section_patterns['precautions'], section)
        preparation_match = re.search(section_patterns['preparation'], section)
        results_match = re.search(section_patterns['results'], section)

        if description_match:
            # Get the description content
            description_start = description_match.end()
            description_end = len(section)

            # Find the end of the description by identifying the next section
            if purpose_match:
                description_end = purpose_match.start()
            elif precautions_match:
                description_end = precautions_match.start()
            elif preparation_match:
                description_end = preparation_match.start()
            elif results_match:
                description_end = results_match.start()

            description_text = section[description_start:description_end].strip()

            # Pair with Definition as summary
            definition_text = section[:description_match.start()].strip()
            pairs.append({
                'text': description_text,
                'summary': definition_text
            })

            # Optionally pair with Purpose as summary
            if purpose_match:
                purpose_text = section[purpose_match.end():precautions_match.start() if precautions_match else len(section)].strip()
                pairs.append({
                    'text': description_text,
                    'summary': purpose_text
                })

            # Optionally pair with Precautions as summary
            if precautions_match:
                precautions_text = section[precautions_match.end():preparation_match.start() if preparation_match else len(section)].strip()
                pairs.append({
                    'text': description_text,
                    'summary': precautions_text
                })

            # Optionally pair with Preparation as summary
            if preparation_match:
                preparation_text = section[preparation_match.end():results_match.start() if results_match else len(section)].strip()
                pairs.append({
                    'text': description_text,
                    'summary': preparation_text
                })

            # Optionally pair with Results as summary
            if results_match:
                results_text = section[results_match.end():].strip()
                pairs.append({
                    'text': description_text,
                    'summary': results_text
                })

    return pairs

# Load the cleaned text
with open("Data/cleaned_medical_text.txt", "r", encoding="utf-8") as f:
    medical_text = f.read()

# Create summarization pairs by experimenting with different section pairings
summarization_pairs = create_summarization_pairs(medical_text)

# Save the summarization pairs to a JSON file
with open("Data/summarization_pairs.json", "w", encoding="utf-8") as f:
    json.dump(summarization_pairs, f)

# Print the first few pairs to verify
print(summarization_pairs[:3])
