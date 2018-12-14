import pandas as pd

print ("hello world")

data = pd.read_csv("salaries-2017.csv") # import csv as a DataFrame

# Data Brief Analysis 
##print(data) # Shows all data
##print(data.shape) # Shows number of columns and rows
##print(data.dtypes) # Shows names of columns and data type
##print(data.describe(include='all')) # Basic descriptive data analysis (count, std, unique ...)
##print(data.head(3)) # Prints top 3 rows
##print(data['Salary Paid']) # Prints out 'Salary Paid' column
##print(data.Sector.unique()) # Show unique values of 'Sector' column

# Convert currency to float single column
##data['Salary Paid'] = data['Salary Paid'].str.replace('$','') # Replace $ with nothing
##data['Salary Paid'] = data['Salary Paid'].str.replace(',','') # Replace , with nothing
##data['Salary Paid']= pd.to_numeric(data['Salary Paid']) # Convert column to numeric value (float64)

# Convert currency to float multiple columns
moneyData = ['Salary Paid', 'Taxable Benefits']
data[moneyData] = data[moneyData].replace('[\$,]','',regex=True) # Replace $ and , with nothing
data[moneyData] = data[moneyData].apply(pd.to_numeric) # Convert data type to numeric
##print(data[['Salary Paid','Taxable Benefits']])
##print(data.dtypes)

# Delete a column 
data = data.drop(['Calendar Year'], axis='columns')
print(data.dtypes)

# Create a column (sum of two other columns)
data['Total Earned'] = data['Salary Paid'] + data['Taxable Benefits']
##print(data[['Salary Paid', 'Taxable Benefits', 'Total Earned']])

