import spacy
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Sample tweets
tweets = [
    "Apple is set to release the new iPhone 14 next month!",
    "Google announces new features for Android at the developer conference.",
    "Microsoft partners with OpenAI to enhance their AI capabilities.",
    "Amazon plans to expand its logistics network globally.",
    "Tesla's latest autopilot update shows impressive improvements.",
    "Facebook rebrands to Meta to focus on the metaverse.",
]

# Load the spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Process the tweets
entities = []
for tweet in tweets:
    doc = nlp(tweet)
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))

# Create a DataFrame for entities
entities_df = pd.DataFrame(entities, columns=["Entity", "Label"])
print(entities_df)

# Count the frequency of each entity
entity_counts = Counter([entity[0] for entity in entities])

# Create a DataFrame for visualization
entity_counts_df = pd.DataFrame(entity_counts.items(), columns=["Entity", "Count"])

# Sort the DataFrame by count
entity_counts_df = entity_counts_df.sort_values(by="Count", ascending=False)

# Plot the trends
plt.figure(figsize=(10, 6))
plt.barh(entity_counts_df["Entity"], entity_counts_df["Count"], color="skyblue")
plt.xlabel("Count")
plt.title("Twitter Trends based on Domain Entity Recognition")
plt.gca().invert_yaxis()
plt.show()
