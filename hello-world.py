import pandas as pd
import seaborn
import matplotlib.pyplot as plt

print ("hello world")

data = pd.read_csv("salaries-2017.csv") # import csv as a DataFrame

# Data Brief Analysis 
##print(data) # All data
##print(data.head(10)) # Top 10 rows
##print(data.tail(10)) # Bottom 10 rows
##print(data.sample(10)) # Random 10 rows
##print(data.shape) # Number of columns and rows
##print(data.dtypes) # Data types by column
##print(data.describe(include='all')) # Basic descriptive data analysis (count, std, unique ...)
##print(data['Salary Paid']) # 'Salary Paid' column
##print(data.isnull().sum()) # Number of null values (blanks or NA) by column
##print(data.isnull().values.any() # Returns boolean True is there is any missing values
##print(data['Last Name'].unique()) # Unique values in a column

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
##print(data.dtypes)

# Create a column (sum of two other columns)
data['Total Earned'] = data['Salary Paid'] + data['Taxable Benefits']
##print(data[['Salary Paid', 'Taxable Benefits', 'Total Earned']])

data['First Name'] = data['First Name'].replace('(Dr\.)','',regex=True) # Remove all Dr.
data['First Name'] = data['First Name'].str.strip() # Remove whitespace before/after string

# Bar Graph - First letter of first name total earnings 
plt.figure(figsize=(20,8)) # Make a figure large enough to fit the screen

data['First Letter'] = data['First Name'].str[0]
data['First Letter'] = data['First Letter'].replace('É','E',regex=False)
##print(data['First Letter'].unique())

(data.groupby("First Letter")['Total Earned'].sum() / sum(data['Total Earned'])).plot(kind='bar', x='First Letter of First Name', y='$', title='Relative Total Earnings by First Letter of First Name 2017')

# Letter J
dataj = data.loc[data['First Letter'].str.startswith('J')]
print(dataj.groupby('First Name')['Total Earned'].sum().nlargest(10)) # Sum of all values in a column by first name

# Letter M
datam = data.loc[data['First Letter'].str.startswith('M')]
print(datam.groupby('First Name')['Total Earned'].sum().nlargest(10)) # Sum of all values in a column by first name

plt.tight_layout() # Show all of the x-axis label
plt.show() # Show the plot

# Extra
print(data.groupby("First Name")['Total Earned'].sum().nlargest(20)) # Reason to guess M because of Michael
##print(data['First Name'].loc[data['First Name'].str.contains(' ')]) # Find rows with certain thing (contains defaults to regex)

# TO DO: show how J is bigger than M... head to head comparison?


