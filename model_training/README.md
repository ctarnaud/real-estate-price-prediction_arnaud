# Importing all the necessary libraries needed for the cleaning and modeling

We used the various libraries from: 
pandas
numpy
sklearn
seaborn
datetime
matplotlib

# Data Cleaning

We started with calculating the age of house/appartment from the construction year.
Making it a column in our dataframe.
Sorted the values by age.
Buildings withh negative ages, such as uncompleted buildings, the ages were replaced with zero
We checked the shape of our dataframe to make sure we are consistent and sure of any changes made.
Next step was checking for Null values and replace them.
Columns that had no price values were dropped because they would be of no value in our analysis.
Proceded with transforming categorical values to continuous values using the map function.

# Data Formating

Now that the dataset is ready, you have to format it for machine learning.
Divide your dataset for training and testing. ( X_train , y_train , X_test , y_test ).

Get the Correlation matrix and plot it.

corr_mat=df_immoweb_clean.corr(method='pearson')
plt.figure(figsize=(20,10))
sns.heatmap(corr_mat,vmax=1,square=True,annot=True,cmap='cubehelix')

From the correlation plot, we notice that there exist multicollinearity (correlation between explanatory variable) between "Type" and 'NetHabitableSurface (msq)','BedroomCount'. This not required by regression, thus we drop "Type".

# Model selection and Step 4: Model training

The dataset is ready. Now let's select a model.
Look at which models make the most sense according to your data.
Since the dependent variable is continuous, we consider some regression models

## Regression Modelling

### Simple Linear Regression

Question: Does the age of a building( Whether House or Appartment) have an EFFECT on the price of a house or can age of a building ALONE be used to predict the price of a building?
Answer: To verify this question, we can do a simplelinear regression usiing Price and age(In this case we use X_Simple).

R-Squared value: We expect this to be close to 1. The value is very low(0.00005) implying that(based on the data) we can not use the age of a house alone to predict the price of the house. We need to add more variables to the model.

### Model 2 : Multiple Linear Regression: Add All regression variable

### Model 3: Random Forest Regressor

# Model Evaluation

We evaluated our model by selecting the most appropriate metrics. Which
performance did you reach?

####                              R-Squared	"    " Root Mean Square Error
#### Simple Linear Regression	    0.000144	"    " 133584.603849
#### Multiple Linear Regression	  0.526711	"    " 91407.212271
#### Random Forest Regressor	    0.927738	"    " 74786.184576

#### Note: Random Forest Regressor has the best performance given it has the lowest RMSE. RMSE  compares the difference between the actual price values in the test set and the predicted price values by our model.

### How could you improve this result?
This results could be improved by adding more features(explanatory variables) and also adding more data for the model to train on. This could help explain more of the variability of housing price.

## Which part of the process has the most impact on the results?

The training part has more impact on the results. This is because the model trains on historical and uses it to predict on new data. If there is not enough data and features, the more learns very little from the data hence a lower predictive power and vice versa.

## How should you divide your time working on this kind of project?

To work on this kind of project, I will allocate more time to collecting data, cleaning and preparing data. This process take a lot more time than generating a model.
