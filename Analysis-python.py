#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
from pybaseball import batting_stats
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Initialize an empty DataFrame
all_years_data = pd.DataFrame()

# Loop through the years of interest
for year in range(2015, 2023):  # 2023 is the stop argument and it's exclusive
    # Fetch batting stats for a given year
    year_data = batting_stats(year)
    
    # Add a 'Year' column to keep track of the year of the data
    year_data['Year'] = year

    # Append the yearly data to the overall DataFrame
    all_years_data = pd.concat([all_years_data, year_data])

# Now 'all_years_data' holds data from 2012 to 2022


# In[18]:


all_years_data.head()


# In[ ]:





# In[19]:


# Load the People.csv file from Lahman's Baseball Database
people_df = pd.read_csv('People.csv')

# Extract playerID and height
height_df = people_df[['playerID', 'height']]

# Display the DataFrame
print(height_df)


# In[20]:


people_df['Name'] = people_df['nameFirst'] + ' ' + people_df['nameLast']


# In[21]:


# Remove leading/trailing white space
people_df['Name'] = people_df['Name'].str.strip()
all_years_data['Name'] = all_years_data['Name'].str.strip()

# Convert to same case (let's go with title case)
people_df['Name'] = people_df['Name'].str.title()
all_years_data['Name'] = all_years_data['Name'].str.title()


# In[22]:


height_df = people_df[['Name', 'height']]


# In[23]:


height_df["height"].describe()


# In[24]:


all_data_with_height = pd.merge(all_years_data, height_df, on='Name', how='inner')


# In[25]:


all_data_with_height.tail()


# In[26]:


# Group# Group by 'Name' and 'height', calculate the mean, then reset index
player_avg_data = all_data_with_height.groupby(['Name', 'height'])[['AVG', 'OBP', 'SLG', 'BB', 'IBB', 'SB']].mean().reset_index()

# Now 'player_avg_data' holds the average performance statistics for each player over the years 2012-2022, 
# along with each player's height


# In[27]:


player_avg_data.describe()


# In[28]:


# Calculate the average height
average_height = height_df['height'].mean()

# Display the average height
print("Average height of players:", average_height)


# In[29]:


def height_category(height):
    if height < 72:  # less than 72 inches
        return 'Short'
    elif height <= 75:  # 73 to 75 inches
        return 'Average'
    else:  # 76 inches and taller
        return 'Tall'

# Apply the function to create a new 'Height Category' column
player_avg_data['Height Category'] = player_avg_data['height'].apply(height_category)


# In[30]:


player_avg_data


# In[31]:


# Set up the matplotlib figure
f, axes = plt.subplots(6, 1, figsize=(7, 15), sharex=True)

sns.barplot(x='Height Category', y='AVG', data=player_avg_data, ax=axes[0])
axes[0].set_ylabel('Average Batting Average')

sns.barplot(x='Height Category', y='OBP', data=player_avg_data, ax=axes[1])
axes[1].set_ylabel('Average On-Base Percentage')

sns.barplot(x='Height Category', y='SLG', data=player_avg_data, ax=axes[2])
axes[2].set_ylabel('Average Slugging Percentage')

sns.barplot(x='Height Category', y='BB', data=player_avg_data, ax=axes[3])
axes[3].set_ylabel('Average Base on Balls')

sns.barplot(x='Height Category', y='IBB', data=player_avg_data, ax=axes[4])
axes[4].set_ylabel('Average Intentional Base on Balls')

sns.barplot(x='Height Category', y='SB', data=player_avg_data, ax=axes[5])
axes[5].set_ylabel('Average Stolen Bases')

plt.tight_layout()


# In[32]:


f, axes = plt.subplots(6, 1, figsize=(7, 15), sharex=True)

sns.boxplot(x='Height Category', y='AVG', data=player_avg_data, ax=axes[0])
axes[0].set_ylabel('Batting Average')

sns.boxplot(x='Height Category', y='OBP', data=player_avg_data, ax=axes[1])
axes[1].set_ylabel('On-Base Percentage')

sns.boxplot(x='Height Category', y='SLG', data=player_avg_data, ax=axes[2])
axes[2].set_ylabel('Slugging Percentage')

sns.boxplot(x='Height Category', y='BB', data=player_avg_data, ax=axes[3])
axes[3].set_ylabel('Base on Balls')

sns.boxplot(x='Height Category', y='IBB', data=player_avg_data, ax=axes[4])
axes[4].set_ylabel('Intentional Base on Balls')

sns.boxplot(x='Height Category', y='SB', data=player_avg_data, ax=axes[5])
axes[5].set_ylabel('Stolen Bases')

plt.tight_layout()



# In[33]:


f, axes = plt.subplots(6, 1, figsize=(7, 15), sharex=True)

sns.scatterplot(x='height', y='AVG', hue='Height Category', data=player_avg_data, ax=axes[0])
axes[0].set_ylabel('Batting Average')

sns.scatterplot(x='height', y='OBP', hue='Height Category', data=player_avg_data, ax=axes[1])
axes[1].set_ylabel('On-Base Percentage')

sns.scatterplot(x='height', y='SLG', hue='Height Category', data=player_avg_data, ax=axes[2])
axes[2].set_ylabel('Slugging Percentage')

sns.scatterplot(x='height', y='BB', hue='Height Category', data=player_avg_data, ax=axes[3])
axes[3].set_ylabel('Base on Balls')

sns.scatterplot(x='height', y='IBB', hue='Height Category', data=player_avg_data, ax=axes[4])
axes[4].set_ylabel('Intentional Base on Balls')

sns.scatterplot(x='height', y='SB', hue='Height Category', data=player_avg_data, ax=axes[5])
axes[5].set_ylabel('Stolen Bases')

plt.tight_layout()


# In[34]:


sns.pairplot(player_avg_data[['AVG', 'OBP', 'SLG', 'BB', 'IBB', 'SB', 'height']])


# In[40]:


# Scatter plot of AVG vs. OBP with green markers
sns.scatterplot(x='AVG', y='OBP', hue='height', data=player_avg_data, color='green')
plt.title('AVG vs. OBP')
plt.show()

# Scatter plot of SLG vs. BB with green markers
sns.scatterplot(x='SLG', y='BB', hue='height', data=player_avg_data, color='green')
plt.title('SLG vs. BB')
plt.show()



# In[ ]:





# In[ ]:




