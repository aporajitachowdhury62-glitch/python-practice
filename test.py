import pandas as pd

# Create a simple dataset
data = {
    'Name': ['Amit', 'Priya', 'Rahul', 'Sneha'],
    'Age': [25, 30, 22, 28],
    'City': ['Mumbai', 'Delhi', 'Nagpur', 'Pune']
}

# Convert it into a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Original Data:")
print(df)

# Basic operations
print("\nFirst 2 rows:")
print(df.head(2))

print("\nAverage age:", df['Age'].mean())

print("\nPeople older than 25:")
print(df[df['Age'] > 25])

# Sort by Age
print("\nSorted by Age:")
print(df.sort_values('Age'))