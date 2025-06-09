import pandas as pd

# Load the CSV
df = pd.read_csv("data/netflix_titles.csv")

pd.set_option('display.max_columns', None)

# Replace missing values in 'country' column with 'Unknown'
df['country'].fillna('Unknown', inplace=True)

# Print the number of missing values remaining in the 'country' column
print("\nNumber of missing values in 'country' column:")
print(df['country'].isnull().sum())

# Export the DataFrame to an Excel file
df.to_excel('netflix_output.xlsx', index=False)

print("Data exported successfully to 'netflix_output.xlsx'")