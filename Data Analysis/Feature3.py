import pandas as pd

try:
    # Load the CSV file into a DataFrame
    file_path = '../Data/reviews_dec18.csv'
    df = pd.read_csv(file_path)

    # Convert the 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Ask the user for the keyword and date range
    keyword = input("Enter the keyword to search for in the 'comments' column: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Convert user-input dates to datetime objects
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    # Filter the DataFrame based on user criteria
    filtered_df = df[(df['date'] >= start_date) & (df['date'] <= end_date) & df['comments'].str.contains(keyword, case=False, na=False)]

    # Display the filtered results
    if filtered_df.empty:
        print("No matching records found.")
    else:
        print(filtered_df)
except FileNotFoundError:
    print("Error: The specified file was not found.")
except ValueError:
    print("Error: Invalid date format. Please use YYYY-MM-DD.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
