
# coding: utf-8

# In[7]:


#Regression
#Introduction to regression
#importing Boston housing data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
boston = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)/Supervised Learning with scikit-learn/Boston housing.csv')
print boston.head()
#Creating feature and target arrays
X = boston.drop('MEDV', axis=1).values
y = boston['MEDV'].values
#predicting house value from a single feature
X_rooms = X[:,5]
print type(X_rooms), type(y)
y = y.reshape(-1,1)
X_rooms = X_rooms.reshape(-1,1)
#Plotting house value vs. number of rooms
plt.scatter(X_rooms,y)
plt.ylabel('Value of house /1000 ($)')
plt.xlabel('Number of rooms')
plt.show()
#Fitting a regression model
reg = linear_model.LinearRegression()
reg.fit(X_rooms,y)
prediction_space = np.linspace(min(X_rooms),max(X_rooms)).reshape(-1,1)
plt.scatter(X_rooms,y,color='blue')
plt.plot(prediction_space, reg.predict(prediction_space), color='black', 
         linewidth=3)
plt.show()


# In[4]:


#Importing data for supervised learning
import numpy as np
import pandas as pd
import seaborn as sns
#Read the CSV file into DataFrame: df
df = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)//Supervised Learning with scikit-learn/Gapminder.csv')
# Knowing your data structure
print df.info()
print df.describe()
print df.head()
# computes the pairwise correlation between columns:
sns.heatmap(df.corr(), square=True, cmap='RdYlGn')
#Create arrays for features and target variable
y = df['life'].values
X = df['fertility'].values
# Print the dimensions of X and y before reshaping
print "Dimensions of y before reshaping: {}".format(y.shape)
print "Dimensions of X before reshaping: {}".format(X.shape)
# Reshape X and y
y = y.reshape(-1,1)
X = X.reshape(-1,1)
# Print the dimensions of X and y after reshaping
print "Dimensions of y after reshaping: {}".format(y.shape)
print "Dimensions of X after reshaping: {}".format(X.shape)
#Getting the feature and target variable arrays into the right format for scikit-learn
#is an important precursor to model building


# In[9]:


# The basics of linear regression (video recap)
'''
Regression mechanics
y = ax + b
y = target
x = single feature
a,b = parameters of model
how do we choose a and b?
Define an error function for any given line, choose the line that minimizes 
the error function

#The loss function, sum of the square of residual: 
Ordinary least squares (OLS), Minimize sum of the squares of residuals

#Linear regression in higher dimensions
y = a1x1 + a2X2 + b
To fit a linear regression model here, need to specify 3 variables: a1,a2,b
In higher dimensions: must specify coefficient for each feature and the variable b 

Scikit-learn API:
pass two arrays: Features, and target
'''
#Linear regression on all features
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.3,                                                    random_state=42)
reg_all = linear_model.LinearRegression()
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test)
# The default storing method for linear regression is called R square
reg_all.score(X_test, y_test)


# In[31]:


#fit and predict for regression
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Preload data
df = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)//Supervised Learning with scikit-learn/Gapminder.csv')
y = df[['life']].values
X_fertility = df[['fertility']].values
# Create the regressor: reg
reg = LinearRegression()
# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)
# Fit the model to the data
reg.fit(X_fertility,y)
# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)
# Print R^2
print reg.score(X_fertility,y)
# Plot regression line
plt.plot(prediction_space, y_pred, color='red', linewidth=3)
plt.show()
'''
line captures the undelying trend in the data, and the performance is quite decent
for this basic regression model with only one feature!
'''


# In[35]:


#Train/test split for regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
df = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)//Supervised Learning with scikit-learn/Gapminder.csv')
y = df[['life']].values
X = df[['fertility']].values
# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.3, random_state=42)
# Create the regressor: reg_all
reg_all = LinearRegression()
# Fit the regressor to the training data
reg_all.fit(X_train, y_train)
# Predict on the test data: y_pred
y_pred = reg_all.predict(X_test)
# Compute and print R^2 and RMSE(Root Mean Squared Error)
print "R^2: {}".format(reg_all.score(X_test, y_test))
rmse = np.sqrt(mean_squared_error(y_test,y_pred))
print "Root Mean Squared Error: {}".format(rmse)


# In[38]:


# Cross-validation video recap
'''
>Cross-validation motivation
Model performance is dependent on way the data is split
Not representative of the model's ability to generalize
Solution: Cross-validation

>Cross-validation
split1 : Fold1(train), Fold2(test), Fold3(test) > Metric1
split2 : Fold1(test), Fold2(train), Fold3(test) > Metric2
split3 : Fold1(test), Fold2(test), Fold3(train) > Metric3
above all can called 3-fold Cross Validation, or 3-fold CV
However, more folds = more computationally expensive
'''
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import numpy as np
reg = LinearRegression()
cv_results = cross_val_score(reg, X, y, cv=5)
print cv_results
print np.mean(cv_results)


# In[2]:


# 5-fold cross-validation
# Cross-validation is a vital step in evaluating a model. 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
df = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)//Supervised Learning with scikit-learn/Gapminder.csv')
y = df[['life']].values
X = df[['population','fertility','HIV','GDP','BMI_female','child_mortality']].values
reg = LinearRegression()
# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg, X, y, cv = 5)
print cv_scores
print "Average 5-fold CV Score: {}".format(np.mean(cv_scores))


# In[4]:


# K-Fold CV comparison
'''
use %timeit to see how long each 3-fold CV takes compared to 10-fold CV by each 
3-fold CV takes compared to 10-fold CV by executing the following cv=3 and cv=10.
'''
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
import numpy as np
import pandas as pd
df = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)//Supervised Learning with scikit-learn/Gapminder.csv')
y = df[['life']].values
X = df[['population','fertility','HIV','GDP','BMI_female','child_mortality']].values
# Create a linear regression object: reg
reg = LinearRegression()
# perform 3-fold CV
cvscores_3 = cross_val_score(reg, X, y, cv=3)
print np.mean(cvscores_3)
get_ipython().magic(u'timeit cvscores_3')
# perform 10-fold CV
cvscores_10 = cross_val_score(reg, X, y, cv=10)
print np.mean(cvscores_10)
get_ipython().magic(u'timeit cvscores_10')


# In[11]:


# Regularized regression video recap
'''
Recall: Linear regression minimizes a loss function
It chooses a coefiicient for each feature variable
Large coefficients can lead to overfitting
Penalizing large coefficients: Regularization

Ridge regression
Alpha: parameter we need to choose
Picking alpha here is similar to picking k in k-NN
Hyperparameter tuning (More in Chapter 3)
Alpha controls model complexity
   >Alpha=0, we get back OLS (can lead to overfitting)
   >very high Alpha, can lead to underfitting
'''
# Ridge regression in scikit-learn
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import pandas as pd
#import data
boston = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)/Supervised Learning with scikit-learn/Boston housing.csv')
#Creating feature and target arrays
X = boston.drop('MEDV', axis=1).values
y = boston['MEDV'].values
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.3,random_state=42)
ridge = Ridge(alpha=0.1, normalize=True)
ridge.fit(X_train, y_train)
ridge_pred = ridge.predict(X_test)

'''
Lasso regression
can be used to select important features of a dataset
Shrinks the coefficients of less important features to exactly 0
'''
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt
# case1
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.3,random_state=42)
lasso = Lasso(alpha=0.1, normalize=True)
lasso.fit(X_train, y_train)
lasso_pred = lasso.predict(X_test)
print lasso.score(X_test,y_test)

# case2
names = boston.drop('MEDV', axis=1).columns
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X,y).coef_
_ = plt.plot(range(len(names)), lasso_coef)
_ = plt.xticks(range(len(names)), names, rotation=60)
_ = plt.ylabel('Coefficients')
plt.show()


# In[35]:


# Regularization I: Lasso
from sklearn.linear_model import Lasso
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)//Supervised Learning with scikit-learn/Gapminder.csv')
y = df['life'].values
X = df[['population','fertility','HIV','CO2','BMI_male','GDP','BMI_female','child_mortality']].values
print X, y
df_columns = df.columns.values
# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4, normalize=True)
# Fit the regressor to the data
lasso.fit(X, y)
# Compute and print the coefficients
lasso_coef = lasso.coef_
print lasso_coef
# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()


# In[38]:


# Regularization II: Ridge
'''
Lasso is great for feature selection, but when building regression models,
Ridge regression should be your first choice
'''
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
# Setup the array of alphas and lists to store scores
alpha_space = np.logspace(-4,0,50)
print alpha_space
ridge_scores = []
ridge_scores_std = []
# Create a ridge regressor: ridge
ridge = Ridge(normalize=True)
# Compute scores over range of alphas
for alpha in alpha_space:
    # Specify the alpha value to use: ridge.alpha
    ridge.alpha = alpha
    # Perform 10-fold CV: ridge_cv_scores
    ridge_cv_scores = cross_val_score(ridge, X, y, cv=10)
    # Append the mean of ridge_cv_scores to ridge_scores
    ridge_scores.append(np.mean(ridge_cv_scores))
    # Append the std of ridge_cv_scores to ridge_scores_std
    ridge_scores_std.append(np.std(ridge_cv_scores))

def display_plot(cv_scores, cv_scores_std):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(alpha_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel('Alpha')
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale('log')
    plt.show()  
    
#display_plot(ridge_scores, ridge_scores_std)
display_plot(ridge_scores, ridge_scores_std)

