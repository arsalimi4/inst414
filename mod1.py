import pandas as pd

# Load the data
data = pd.read_csv('cardata.csv')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Check for any missing values
print(data.isnull().sum())

# Finding the most frequently appearing car model
most_frequent_model = data["Company"].mode()[0]
frequency_of_model = data["Company"].value_counts().loc[most_frequent_model]

print(f"The most frequently appearing car model is '{most_frequent_model}' with {frequency_of_model} appearances.")

# Optionally, you can also view the number of times each model appears
print(data['Company'].value_counts())

print(data.head())

# Check for any missing values
print(data.isnull().sum())

# Grouping the data by 'company' and getting the most common 'location' for each company
most_common_location = data.groupby('Company')['Dealer_Region'].agg(lambda x: x.mode()[0])

print("Most common location for each company:")
print(most_common_location)


print(data.head())

# Check for any missing values
print(data.isnull().sum())

# Grouping the data by 'company' and getting the most common 'location' for each company
most_common_location = data.groupby('Company')['Dealer_Region'].agg(lambda x: x.mode()[0])

print("Most common location for each company:")
print(most_common_location)