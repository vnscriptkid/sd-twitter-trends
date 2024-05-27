import math
from collections import Counter

# Example corpus
corpus = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are great pets"
]

# Preprocess the corpus
documents = [doc.split() for doc in corpus]

# Function to compute term frequency
def compute_tf(document):
    tf_dict = {}
    total_terms = len(document)
    term_counts = Counter(document)
    for term, count in term_counts.items():
        tf_dict[term] = count / total_terms
    return tf_dict

# Function to compute inverse document frequency
def compute_idf(documents):
    N = len(documents)
    idf_dict = {}
    all_terms = set(term for document in documents for term in document)
    for term in all_terms:
        containing_docs = sum(1 for document in documents if term in document)
        idf_dict[term] = math.log(N / (1 + containing_docs))
    return idf_dict

# Compute TF for each document
tf_documents = [compute_tf(doc) for doc in documents]

# Compute IDF for all terms
idf_dict = compute_idf(documents)

# Compute TF-IDF
def compute_tfidf(tf_document, idf_dict):
    tfidf_dict = {}
    for term, tf in tf_document.items():
        tfidf_dict[term] = tf * idf_dict.get(term, 0)
    return tfidf_dict

tfidf_documents = [compute_tfidf(tf_doc, idf_dict) for tf_doc in tf_documents]

# Display the results
for i, tfidf_doc in enumerate(tfidf_documents):
    print(f"Document {i + 1} TF-IDF:")
    for term, tfidf in tfidf_doc.items():
        print(f"  {term}: {tfidf:.4f}")

# Document 1 TF-IDF:
#   the: 0.0000
#   cat: 0.0676
#   sat: 0.0000
#   on: 0.0000
#   mat: 0.0676
# Document 2 TF-IDF:
#   the: 0.0000
#   dog: 0.0676
#   sat: 0.0000
#   on: 0.0000
#   log: 0.0676
# Document 3 TF-IDF:
#   cats: 0.0676
#   and: 0.0676
#   dogs: 0.0676
#   are: 0.0676
#   great: 0.0676
#   pets: 0.0676