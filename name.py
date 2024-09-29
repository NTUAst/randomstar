import pandas as pd

# Load the CSV file
file_path = 'star.csv'
star_data = pd.read_csv(file_path)

# Filter out rows where 'magnitude' column is not numeric
star_data = star_data[pd.to_numeric(star_data["magnitude"], errors='coerce').notnull()]

# Convert each row to a dictionary with specified keys and ensure 'magnitude' is a float
star_list = [
    {"name": row["name"], "magnitude": float(row["magnitude"]), "constellation": row["constellation"]}
    for _, row in star_data.iterrows()
]

# Output the result
print(star_list)  # Display the first 5 entries
