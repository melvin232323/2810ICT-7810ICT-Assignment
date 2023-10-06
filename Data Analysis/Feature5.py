import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame (Update the file path accordingly)
try:
    df = pd.read_csv('./Data/reviews_dec18.csv')
except FileNotFoundError:
    print("Error: The CSV file could not be found.")
    exit()

# Convert the "date" column to a datetime data type
try:
    df['review_date'] = pd.to_datetime(df['date'])
except KeyError:
    print("Error: 'date' column not found in the CSV.")
    exit()

# Group the data by month and count the number of reviews in each month
try:
    monthly_review_counts = df.groupby(df['review_date'].dt.to_period("M")).size()
except KeyError:
    print("Error: 'review_date' column not found in the DataFrame.")
    exit()

# Plot a line graph to visualize the trend
plt.figure(figsize=(10, 6))
monthly_review_counts.plot(kind='line')
plt.title('Customer Review Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Reviews')
plt.show()