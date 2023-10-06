import pandas as pd
import re

# Load the CSV file into a DataFrame
df = pd.read_csv('./Data/reviews_dec18.csv')

#Define a list of keywords related to cleanliness
cleanliness_keywords = ['clean', 'tidy', 'hygiene', 'sanitary', 'spotless', 'neat', 'well-maintained', 'sterile']

# Function to check if a comment contains any of the cleanliness keywords
def has_cleanliness_keyword(comment):
    if isinstance(comment, str):  # Check if comment is a string
        for keyword in cleanliness_keywords:
            if re.search(r'\b{}\b'.format(keyword), comment, flags=re.IGNORECASE):
                return True
    return False

# Filter comments related to cleanliness and count them
cleanliness_comments = df[df['comments'].apply(has_cleanliness_keyword)]
cleanliness_comment_count = len(cleanliness_comments)

# Print the count of comments related to cleanliness
print(f"Number of comments related to cleanliness: {cleanliness_comment_count}")
