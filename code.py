import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

url='https://assets.datacamp.com/production/course_2023/datasets/gapminder.csv'
df = pd.read_csv(url)

df=df.melt(id_vars='Life expectancy')
df=df.dropna()
df=df[df['variable']!='Unnamed: 0']

df = df.sort_values('Unnamed: 0')
df = df.reset_index(drop=True)
df.columns=['Country','Year','Life_expectancy']

# Add first subplot
plt.subplot(2, 1, 1) 


# Create a histogram of life_expectancy
df['Life_expectancy'].plot(kind='hist')

# Group gapminder: df
df = df.groupby('Year')['Life_expectancy'].mean()

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
df.plot()

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()
plt.savefig('gapminder.png')

# Save both DataFrames to csv files
df.to_csv('gapminder.csv')
df.to_csv('gapminder_agg.csv')


