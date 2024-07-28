# Open the original file and read its contents
file_path = "/Users/sarahgolden/Desktop/SMWapp/stocks/data/S&P500.csv"
with open('S&P500.csv', 'r') as file:
    data = file.read()

# Replace all quotation marks with an empty string
data = data.replace('"', '')

# Write the cleaned data back to the file (or a new file if you prefer)
with open('S&P500.csv', 'w') as file:
    file.write(data)

print("Quotation marks removed successfully.")
