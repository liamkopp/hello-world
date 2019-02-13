import pandas as pd
import seaborn
import matplotlib.pyplot as plt

data = pd.read_csv("public-salaries-2017-gender.csv") # import csv as a DataFrame

print ("hello world")

# DATA BRIEF ANALYSIS 
##print(data) # All data
##print(list(data)) # Names of columns
##print(data.head(10)) # Top 10 rows
##print(data.tail(10)) # Bottom 10 rows
##print(data.sample(10)) # Random 10 rows
##print(data.shape) # Number of columns and rows
##print(data.dtypes) # Data types by column
##print(data.describe(include='all')) # Basic descriptive data analysis (count, std, unique ...)
##print(data['Salary Paid']) # 'Salary Paid' column
##data['Salary Paid'].type # It is a series
##print(data.isnull().sum()) # Number of null values (blanks or NA) by column
##print(data.isnull().values.any() # Returns boolean True if there is any missing values
##print(data['Sector'].unique()) # Unique values in a column

# EXPLAIN INDEX

# DELETE A COLUMN 
data = data.drop(['Calendar Year'], axis='columns')
##print(data.columns) # Show data has no Calendar Year column

# CONVERT CURRENCY TO FLOAT SINGLE COLUMN
# data['Salary Paid'] is a SERIES
data['Salary Paid'] = data['Salary Paid'].str.replace('$','') # (str is for substring) Replace $ with nothing
data['Salary Paid'] = data['Salary Paid'].str.replace(',','') # Replace , with nothing
data['Salary Paid']= pd.to_numeric(data['Salary Paid']) # Convert column to numeric value (float64)
##print(data['Salary Paid'])
##print(data.dtypes) # Show that the column is now type float64
data['Taxable Benefits'] = data['Taxable Benefits'].str.replace('$','') # Replace $ with nothing
data['Taxable Benefits'] = data['Taxable Benefits'].str.replace(',','') # Replace , with nothing
data['Taxable Benefits']= pd.to_numeric(data['Taxable Benefits']) # Convert column to numeric value (float64)
moneyData = data[['Salary Paid', 'Taxable Benefits']] # this is a DATAFRAME
print(moneyData) # Show data now has no $

# CREATE A COLUMN (SUM OF TWO OTHER COLUMNS)
data['Total Earned'] = data['Salary Paid'] + data['Taxable Benefits']
##print(data[['Salary Paid', 'Taxable Benefits', 'Total Earned']]) # Show the addition 

# SHOW TOP 10 HIGHEST EARNERS AND GENDER
top_10_earners = data.nlargest(10, 'Total Earned')
top_10_earners_gender = top_10_earners['Gender'] # There is 1 female
#print(top_10_earners_gender)

# NUMBER OF WOMEN IN TOP 100 
top_100_earners = data.nlargest(100, 'Total Earned')
women_in_top_100 = top_100_earners[top_100_earners['Gender'] == 'f'] # Conditional selection
#print(women_in_top_100)
number_women_in_top_100 = len(women_in_top_100) # There are 22
#print(number_women_in_top_100) 

# SHOW AVERAGE EARNED BY GENDER
gender_group = data.groupby('Gender')
print(gender_group) # <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x7f3863f24fd0>
print(gender_group.groups) # Shows indexes of rows that fall into each group
avg_earnings_by_gender = gender_group.mean() # Automatically averages all numerical columns
#avg_earnings_by_gender_plot = avg_earnings_by_gender['Total Earned'].plot.bar()



# PERCENTAGE OF WOMEN IN TOP 100 BY SECTOR
# Clean up sectors - all seconded falls under government ministry
#print(data.Sector.unique())
data['Sector'] = data['Sector'].str.strip()
data['Sector'] = data['Sector'].str.replace(r'Seconded .*', 'Government of Ontario - Ministries')
#print(data.Sector.unique())

top_100_earners_sector = data.sort_values(by='Total Earned', ascending=False).groupby('Sector').head(100)
#print(top_100_earners_sector)
top_100_earners_sector = top_100_earners_sector.reset_index(drop=True) # Reset_index resets to 0...len(data)-1
#print(top_100_earners_sector)

top_100_earners_sector_gender = top_100_earners_sector.groupby(['Sector', 'Gender'])['Total Earned'].count().unstack().sort_values(by='f')

top_100_earners_sector_gender_percentage_plot = top_100_earners_sector_gender.plot.barh(stacked=True, )
plt.title('Percentage of Women in Top 100 Earners')
plt.xlabel('Percentage (%)')
plt.tight_layout()


# AVG PER GENDER BY SECTOR
avg_earnings_by_gender_sector = data.groupby(['Sector', 'Gender'])['Total Earned'].mean()
#avg_earnings_by_gender_sector_plot = avg_earnings_by_gender_sector.unstack().plot.bar()
#print(avg_earnings_by_gender_sector)

diff_avg_earnings_by_gender_sector = data.groupby(['Sector', 'Gender'])[['Total Earned']].mean().diff()
diff_avg_earnings_by_gender_sector = diff_avg_earnings_by_gender_sector.iloc[1::2].reset_index().rename(columns={'Total Earned':'Difference in Earnings'}).sort_values(by='Difference in Earnings', ascending=False).plot.barh(x='Sector', y='Difference in Earnings')
plt.title('Difference in Mean Earnings between Gender')
plt.xlabel('Difference in Mean Earnings ($)')
plt.tight_layout() # Show all of the x-axis label



#plt.figure(figsize=(20,8)) # Make a figure large enough to fit the screen

plt.show() # Show the plot

