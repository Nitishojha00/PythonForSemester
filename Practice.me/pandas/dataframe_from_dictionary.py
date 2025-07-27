import pandas as pd

# Simple dictionary
data = {
    'Name': ['Nitish', 'Aman', 'Ravi'],
    'Age': [20, 21, 22]
}


# Create DataFrame using the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
