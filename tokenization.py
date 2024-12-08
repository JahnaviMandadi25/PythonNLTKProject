# Import required libraries
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from docx import Document

# Download the necessary NLTK tokenizer models
nltk.download("punkt")

# Load the Word document
doc = Document('/Users/jahnavimandadi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Depression In Animals/Investigating Emotional Distress Across Species.docx')

# Extract text from the document
story = ""
for paragraph in doc.paragraphs:
    story += paragraph.text + " "  # Add each paragraph's text with a space

# Tokenize the text into words
word_tokenized = word_tokenize(story)

# Tokenize the text into sentences
sent_tokenized = sent_tokenize(story)

# Print the results of tokenization
print("---- Word tokenize ----\n", word_tokenized)
print("\n---- Sentence tokenize ----\n", sent_tokenized)
