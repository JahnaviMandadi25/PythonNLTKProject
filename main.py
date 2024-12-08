# Import required libraries
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from docx import Document
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
# Download the necessary NLTK tokenizer models
nltk.download("punkt")
# Download the part-of-speech tagger from NLTK
nltk.download('averaged_perceptron_tagger')
# Download the WordNet resource, used by the lemmatizer
nltk.download('wordnet')

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
nltk.download('stopwords')

stop_words = stopwords.words('english')

filtered_words = []
# Create a list of words from 'story' that are not stopwords
filtered_list = [word for word in word_tokenize(story) if word.casefold() not in stop_words]

# Display the filtered list
print('list of words:',filtered_list)

stemmer = PorterStemmer()

stemmed_words = [stemmer.stem(word) for word in filtered_list]

print('list of stemmed words:',stemmed_words)

tagged_words = nltk.pos_tag(filtered_list)
print('POS Tagged Words:', tagged_words)


# Create an instance of the WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Apply lemmatization to each word in the list of stemmed words
lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]

# Display the lemmatized words
print('Lemmatized words:',lemmatized_words)

fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(18,5),
                        gridspec_kw={"height_ratios": [1],
                                     "hspace": 0.7})
fdist = nltk.FreqDist(stemmed_words)
top_30_words = fdist.most_common(30)
axs.bar([word[0] for word in top_30_words], [word[1] for word in top_30_words])
for i in range(len(top_30_words)):
    axs.text(i, top_30_words[i][1], str(top_30_words[i][1]))
axs.set_xticklabels([word[0] for word in top_30_words], rotation=45)
axs.set_title("Top 30 Words")
axs.set_xlabel("Word")
axs.set_ylabel("Count of Words")
plt.show()

# Create another subplot for the word cloud
fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(10,20),
                        gridspec_kw={"height_ratios": [1],
                                     "hspace": 0.7})

# Generate a word cloud from the frequency distribution of words
wordcloud = WordCloud(width = 800, height = 300,
                background_color ="white",
                stopwords = stopwords.words("english"),
                min_font_size = 10).generate_from_frequencies(fdist)

# Configure the plot settings for the word cloud
plt.figure(figsize = (8, 8), facecolor = None)
axs.imshow(wordcloud)
axs.axis("off")
axs.set_title("Word Cloud-Size indicates frequency")
plt.show()