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
##print(data.isnull().sum()) # Number of null values (blanks or NA) by column
##print(data.isnull().values.any() # Returns boolean True if there is any missing values
##print(data['Last Name'].unique()) # Unique values in a column

# CONVERT CURRENCY TO FLOAT SINGLE COLUMN
##data['Salary Paid'] = data['Salary Paid'].str.replace('$','') # Replace $ with nothing
##data['Salary Paid'] = data['Salary Paid'].str.replace(',','') # Replace , with nothing
##data['Salary Paid']= pd.to_numeric(data['Salary Paid']) # Convert column to numeric value (float64)

# CONVERT CURRENCY TO FLOAT MULTIPLE COLUMNS
moneyData = ['Salary Paid', 'Taxable Benefits']
data[moneyData] = data[moneyData].replace('[\$,]','',regex=True) # Replace $ and , with nothing
data[moneyData] = data[moneyData].apply(pd.to_numeric) # Convert data type to numeric
##print(data[['Salary Paid','Taxable Benefits']]) # Show data now has no $
##print(data.dtypes) # Show that the column is now type float64

# DELETE A COLUMN 
data = data.drop(['Calendar Year'], axis='columns')
##print(list(data)) # Show data has no Calendar Year column

# CREATE A COLUMN (SUM OF TWO OTHER COLUMNS)
data['Total Earned'] = data['Salary Paid'] + data['Taxable Benefits']
##print(data[['Salary Paid', 'Taxable Benefits', 'Total Earned']]) # Show the addition 

# SHOW TOP 10 HIGHEST EARNERS AND GENDER
top_10_earners = data.nlargest(10, 'Total Earned')
top_10_earners_gender = top_10_earners['Gender'] # There is 1 female
#print(top_10_earners_gender)

# NUMBER OF WOMEN IN TOP 100 
top_100_earners = data.nlargest(100, 'Total Earned')
women_in_top_100 = top_100_earners[top_100_earners['Gender'] == 'f']
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
top_100_earners_sector = top_100_earners_sector.reset_index(drop=True)
#print(top_100_earners_sector)

top_100_earners_sector_gender = top_100_earners_sector.groupby(['Sector', 'Gender'])['Total Earned'].count().unstack().sort_values(by='f')

top_100_earners_sector_gender_percentage_plot = top_100_earners_sector_gender.plot.barh(stacked=True, )





# PERCENTAGE OF WOMEN BY SECTOR?

# AVG PER GENDER BY SECTOR
avg_earnings_by_gender_sector = data.groupby(['Sector', 'Gender'])['Total Earned'].mean()
#avg_earnings_by_gender_sector_plot = avg_earnings_by_gender_sector.unstack().plot.bar()
#print(avg_earnings_by_gender_sector)

#fig2=plt.figure()
plt.tight_layout()
new_avg_earnings_by_gender_sector = data.groupby(['Sector', 'Gender'])[['Total Earned']].mean().diff()#.plot.bar()
new_avg_earnings_by_gender_sector = new_avg_earnings_by_gender_sector.iloc[1::2].reset_index().rename(columns={'Total Earned':'Difference in Earnings'}).sort_values(by='Difference in Earnings', ascending=False).plot.barh(x='Sector', y='Difference in Earnings')
print(new_avg_earnings_by_gender_sector)

# Bar Graph 
#plt.figure(figsize=(20,8)) # Make a figure large enough to fit the screen

plt.tight_layout() # Show all of the x-axis label
plt.show() # Show the plot

# Extra
#print(data.groupby("First Name")['Total Earned'].sum().nlargest(20)) # Reason to guess M because of Michael
##print(data['First Name'].loc[data['First Name'].str.contains(' ')]) # Find rows with certain thing (contains defaults to regex)

# TO DO: show how J is bigger than M... head to head comparison?


