import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Predefined topics
topics = ["Sports", "Politics", "Technology", "Entertainment", "Health"]

# Sample tweets data
tweets = [
    "The football match last night was thrilling!",
    "The new tech gadget is revolutionary.",
    "A major political event happened today.",
    "The latest movie in the series is fantastic!",
    "Health benefits of a balanced diet are immense.",
    "The basketball game was intense!",
    "Tech companies are innovating rapidly.",
    "Political discussions are heating up.",
    "New entertainment options are emerging.",
    "Health care advancements are impressive."
]

# Step 2: Data Preprocessing
def preprocess_text(text):
    # Basic text cleaning can be added here
    return text.lower()

preprocessed_tweets = [preprocess_text(tweet) for tweet in tweets]

# Step 3: Feature Extraction using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(preprocessed_tweets)

# Step 4: Clustering using k-means
num_clusters = len(topics)
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Assigning labels to each tweet
labels = kmeans.labels_

# Creating a DataFrame for better visualization
df = pd.DataFrame({'Tweet': tweets, 'Cluster': labels})

# Mapping cluster labels to topics
df['Topic'] = df['Cluster'].map(lambda x: topics[x])

# Display the clustered tweets
print(df)

# Plotting the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x=X.toarray()[:, 0], y=X.toarray()[:, 1], hue=labels, palette='viridis')
plt.title('K-means Clustering of Tweets')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

#                                              Tweet  Cluster          Topic
# 0     The football match last night was thrilling!        3  Entertainment
# 1            The new tech gadget is revolutionary.        2     Technology
# 2          A major political event happened today.        3  Entertainment
# 3     The latest movie in the series is fantastic!        0         Sports
# 4  Health benefits of a balanced diet are immense.        4         Health
# 5                 The basketball game was intense!        3  Entertainment
# 6           Tech companies are innovating rapidly.        1       Politics
# 7            Political discussions are heating up.        3  Entertainment
# 8          New entertainment options are emerging.        2     Technology
# 9         Health care advancements are impressive.        4         Health