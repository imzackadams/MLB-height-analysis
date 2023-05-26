#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
from pybaseball import batting_stats

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# Initialize an empty DataFrame
all_years_data = pd.DataFrame()

# Loop through the years of interest
for year in range(2018, 2023):  # 2023 is the stop argument and it's exclusive
    # Fetch batting stats for a given year
    year_data = batting_stats(year)
    
    # Add a 'Year' column to keep track of the year of the data
    year_data['Year'] = year

    # Append the yearly data to the overall DataFrame
    all_years_data = pd.concat([all_years_data, year_data])

# Now 'all_years_data' holds data from 2018 to 2022


# In[8]:


all_years_data.head()


# In[ ]:





# In[9]:


# Load the People.csv file from Lahman's Baseball Database
people_df = pd.read_csv('People.csv')

# Extract playerID and height
height_df = people_df[['playerID', 'height']]

# Display the DataFrame
print(height_df)


# In[10]:


people_df['Name'] = people_df['nameFirst'] + ' ' + people_df['nameLast']


# In[11]:


# Remove leading/trailing white space
people_df['Name'] = people_df['Name'].str.strip()
all_years_data['Name'] = all_years_data['Name'].str.strip()

# Convert to same case (let's go with title case)
people_df['Name'] = people_df['Name'].str.title()
all_years_data['Name'] = all_years_data['Name'].str.title()


# In[12]:


height_df = people_df[['Name', 'height']]


# In[15]:


height_df.head()


# In[16]:


all_data_with_height = pd.merge(all_years_data, height_df, on='Name', how='inner')


# In[18]:


all_data_with_height


# In[22]:


# Group# Group by 'Name' and 'height', calculate the mean, then reset index
player_avg_data = all_data_with_height.groupby(['Name', 'height'])[['AVG', 'OBP', 'SLG']].mean().reset_index()

# Now 'player_avg_data' holds the average performance statistics for each player over the years 2018-2022, 
# along with each player's height


# In[23]:


player_avg_data


# In[ ]:




