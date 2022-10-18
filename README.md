# real-estate-price-prediction_arnaud
Second web scraping and data analysis challenge
Start by importng the necessary libraries needed to clean the data and to make inferences like plots
We imported the following libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import seaborn as sns
import warnings

warnings.filterwarnings("ignore")

# Download and use dataframe
df_immoweb = pd.read_csv('immoweb_BE.csv')
displayed the head to get an overview of the dataframe
df_immoweb.head()

# Exploring the dataframe
We used the various synthaxes to like describe, info, shape, dtypes, to understand and to be able to work with our dataframe

# Checking the percentate missing values
(df_immoweb.isnull().sum(axis = 0)* 100 / len(df_immoweb)).sort_values(ascending=True)

# Which variables would you delete and why ?
Notice from above that dropping null values results to an empty dataframe. Further investigations are carried out
All columns with more 80% missing values will be removed since they carry no information.

# Splitting the datafeame to get a detail understnding of the missing values
Notice that when we split the dataframes on the basis of types(House or Apartment) while looking at missing values, it becomes immediately clear that "land_surface" is missing for all apartments(all 4190 observations) it will be advicable to drop such a variable from the analysis since it may cause bias. Same applies for "wellnessEquipment_hasSwimmingPool", "condition_isNewlyBuilt", "outdoor_garden_surface"

(df_apartment.isnull().sum(axis = 0)* 100 / len(df_apartment)).sort_values(ascending=True)
print(len(df_apartment))
and do the same for house

# Identifying outlier and removing them 
We identified and removed outliers to avoid bias in our analysis

# Plot
We then proceed with various plots for visualization

