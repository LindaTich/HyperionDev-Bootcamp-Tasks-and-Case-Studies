'''Start
Create a file sentiment_analysis in python.
Import Pandas library as pd.
Import spaCy library.
Import TextBlob library.
Load the spaCy model 'en_core_web_sm'.
Load the dataset using pandas.
Save it as amazon_product_reviews.csv.
Preprocess text data and apply to the text.
Remove the rows with empty cleaned text.
Create a function for sentiment analysis.
Create sample review for analysing function.
Perform sentiment analysis on the sample.
Compare sentiment of two reviews.
These are represented by indexes using similarity().
Create sample review indexes for comparison.
Compare sentiments of the two reviews.
Write a brief summary on the results.
Save as PDF document.
Call it 'sentiment_analysis_report.pdf'
End'''

# Import spaCy 

# Import pandas

import pandas as pd
import spacy
# from spacytextblob import TextBlob
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the spaCy'en_core_web_sm' model
nlp = spacy.load('en_core_web_sm')

# Load the dataset
df = pd.read_csv('amazon_product_reviews.csv')

# Preprocess text data
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Strip leading and trailing whitespaces
    text = text.strip()
    # Remove stopwords
    doc = nlp(text)
    text = ' '.join([token.text for token in doc if not token.is_stop])
    return text

# Apply preprocessing to text data
df['cleaned_text'] = df['review_text'].apply(preprocess_text)

# Remove rows with empty cleaned text
df = df.dropna(subset=['cleaned_text'])

# Function for sentiment analysis
def sentiment_analysis(text):
    # Create a spaCy Doc object
    doc = nlp(text)
    
    # Perform sentiment analysis
    tb = TextBlob(doc._.polarity)
    sentiment = tb.sentiment

    return sentiment

# Sample review for testing sentiment analysis function
sample_review = "This product is great!"

# Sentiment analysis on the sample review
sample_sentiment = sentiment_analysis(sample_review)
print("Sample Review Sentiment:", sample_sentiment)

# Compare sentiment of two reviews represented by indexes using similarity
def compare_reviews(index1, index2):
    # Get the texts of the reviews
    text1 = df.loc[index1, 'cleaned_text']
    text2 = df.loc[index2, 'cleaned_text']

    # Perform sentiment analysis on the reviews
    sentiment1 = sentiment_analysis(text1)
    sentiment2 = sentiment_analysis(text2)

    # Calculate similarity between sentiments
    similarity = sentiment1.similarity(sentiment2)

    return similarity

# Sample review indexes for comparison
index1 = 0
index2 = 1

# Compare sentiments of the two reviews
similarity_score = compare_reviews(index1, index2)
print("Similarity between review {} and review {}: {}".format(index1, index2, similarity_score))


