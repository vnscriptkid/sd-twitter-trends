import os
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Function to read all files in the ./articles directory
def read_articles(directory):
    articles = []
    filenames = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                articles.append(file.read())
                filenames.append(filename)
    return articles, filenames

# Directory containing the articles
directory = './articles'

# Read the articles
articles, filenames = read_articles(directory)

# Perform TF-IDF analysis
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(articles)
terms = vectorizer.get_feature_names_out()

# Convert the TF-IDF matrix to a DataFrame for better visualization
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), index=filenames, columns=terms)

# Display the DataFrame
print(tfidf_df.head())

# Optionally, save the DataFrame to a CSV file for later analysis
# tfidf_df.to_csv('tfidf_analysis.csv')

# Identify Key Terms in Documents
# Example: Identify key terms in article1.txt (document 0)
article1_tfidf = tfidf_df.loc['technology.txt']
key_terms_article1 = article1_tfidf[article1_tfidf > 0].sort_values(ascending=False)
print("\nKey terms in technology.txt:")
print(key_terms_article1.head(10))  # Display top 10 key terms

# Compare Term Importance Across Documents
# Example: Compare the importance of the term 'healthcare' across all documents
term_importance_healthcare = tfidf_df['healthcare']
print("\nImportance of the term 'healthcare' across all documents:")
print(term_importance_healthcare)

# Find Unique Terms
# Example: Find terms that are unique to article1.txt (appear in article1.txt but not in others)
unique_terms_article1 = article1_tfidf[article1_tfidf > 0][article1_tfidf == tfidf_df.max(axis=0)]
print("\nUnique terms in article1.txt:")
print(unique_terms_article1)
