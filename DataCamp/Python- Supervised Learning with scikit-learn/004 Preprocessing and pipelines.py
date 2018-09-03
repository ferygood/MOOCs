
# coding: utf-8

# In[1]:


# Preprocessing data (video recap)
'''
Previous chapter, I have learnt how to implement both classification and regression 
models and how to measure model performance. Also, how to tune hyperparameters 
in order to improve performance.

How to deal with relatively complicated data?
You will have to preprocess your data before you can build models.
For example:
Dealing with categorical features(red,blue,male,female.....)
> these are not numerical values, therefore, the scikit-learn API will not accept.
Solution:
Need to encode categorical features numerically. Convert to 'dummy variables'
0: Observation was NOT that category
1: Observation was that category

Dealing with categorical features in Python
scikit-learn: OneHotEncoder()
pandas: get_dummies()
'''
# Encoding dummy variables
import pandas as pd
df = pd.read_csv('')
df_origin = pd.get_dummies(df)
print (df_origin.head())
# drop the uneeded dummy variable
df_origin = df_origin.drop('origin_Asia', axis=1) 

#Linear regression with dummy varibales
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3
                                                    , random_state=42)
ridge = Ridge(alpha=0.5, normalize=True).fit(X_train, y_train)
ridge.score(X_test,y_test)


# In[9]:


# Handling missing data (video recap)
import pandas as pd
import numpy as np
# load PIMA Indians dataset
df = pd.read_csv('D:R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)/Supervised Learning with scikit-learn/Diabetes.csv')
print (df.info())
print (df.head())
# some value = 0, regard as missing values
# replace missing value as NaN
df.insulin.replace(0, np.nan, inplace=True)
df.triceps.replace(0, np.nan, inplace=True)
df.bmi.replace(0, np.nan, inplace=True)
print (df.head())

# drop all rows containing missing data
df = df.dropna() # sometimes it will drop too many data, and it is unacceptable

# imputing missing data
# Making an educated guess about the missing values
# Example: using the mean of the non-missing entries
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NAN', strategy='mean', axis=0)
imp.fit(X)
X = imp.transform(X)

# Imputing within a pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
logreg = LogisticRegression()
# 2-tuple containing the name you wish to give the relevent step and the estimator.
steps = [('imputation', imp), ('logistic_regression', logreg)]
# pass the list to the pipeline constructor
pipeline = Pipeline(steps)
X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.3, random_state=42)
pipeline.fit(X_train, y_train)
y_pred =  pipeline.predict(X_test)
pipline.score(X_test, y_test)


# In[13]:


# Centering and scaling (video recap)
import pandas as pd
df = pd.read_csv('D:R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)/Supervised Learning with scikit-learn/Red wine quality.csv')
print (df.describe())

'''
Why scale your data?
Many models use some form of distance to inform them
Features on larger scales can unduly influence the model
EX:
k-NN uses distance explicity when making predictions
Therefore, we want features to be on a similar scale
Solution is to do Normalizing (also called scaling or centering)

Ways to normalize your data
(1) Standardization: Subtract the mean and divide by variance. All features are centered
                 around zero and have variance one
(2) Can also subtract the minimum and divide by the range. Minimum zero and maximum one
(3) Can also normalize so the data ranges from -1 to +1
'''
# Scaling in scikit-learn
from sklearn.preprocessing import scale
# pass the feature data to scale and this returns our scaled data
X_scaled = scale(X)
np.mean(X), np.std(X)
np.mean(X_scaled), np.std(X_scaled)
# put scaler in a pipeline
from sklearn.preprocessing import StandardScaler
steps = [('scaler',StandardScalar(), ('knn', KNeighborsClassifier()))]
pipeline = Pipline(steps)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random=21)
knn_scaled = pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print accuarcy_score(y_test,y_pred)
knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)
print knn_unscaled.score(X_test, y_test)

# CV and scaling in a pipeline
steps = [('scaler', StandardScaler()),('knn', KNeighborsClassifier())]
pipeline = Pipline(steps)
parameters = {knn__n_neighbors = np.arange(1,50)}
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random=21)
cv = GridSearchCV(pipeline, param_grid=parameters)
cv.fit(X_train, y_train)
y_pred = cv.predict(X_test)
print (cv.best_params_)
print (cv.score(X_test, y_test))
print (classification_report(y_test, y_pred))


# In[ ]:


# Centering and scaling your data
# Import scale
from sklearn.preprocessing import scale

# Scale the features: X_scaled
X_scaled = scale(X)
# Print the mean and standard deviation of the unscaled features
print("Mean of Unscaled Features: {}".format(np.mean(X))) 
print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))
# Print the mean and standard deviation of the scaled features
print("Mean of Scaled Features: {}".format(np.mean(X_scaled))) 
print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))


# In[ ]:


# Centering and scaling in a pipeline
# Import the necessary modules
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Setup the pipeline steps: steps
steps = [('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier())]
# Create the pipeline: pipeline
pipeline = Pipeline(steps)
# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=42)
# Fit the pipeline to the training set: knn_scaled
knn_scaled = pipeline.fit(X_train,y_train)
# Instantiate and fit a k-NN classifier to the unscaled data
knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)
# Compute and print metrics
print('Accuracy with Scaling: {}'.format(knn_scaled.score(X_test,y_test)))
print('Accuracy without Scaling: {}'.format(knn_unscaled.score(X_test,y_test)))


# In[ ]:


# Bringing it all together I: Pipeline for classification
# Setup the pipeline
steps = [('scaler', StandardScaler()),
         ('SVM', SVC())]
pipeline = Pipeline(steps)
# Specify the hyperparameter space
parameters = {'SVM__C':[1, 10, 100],
              'SVM__gamma':[0.1, 0.01]}
# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=21)
# Instantiate the GridSearchCV object: cv
cv = GridSearchCV(pipeline,param_grid=parameters)
# Fit to the training set
cv.fit(X_train,y_train)
# Predict the labels of the test set: y_pred
y_pred = cv.predict(X_test)
# Compute and print metrics
print("Accuracy: {}".format(cv.score(X_test, y_test)))
print(classification_report(y_test, y_pred))
print("Tuned Model Parameters: {}".format(cv.best_params_))


# In[ ]:


# Bring it all together II: Pipeline for regression
# Setup the pipeline steps: steps
steps = [('Imputation', Imputer(missing_values='NaN', strategy='mean', axis=0)),
         ('scaler', StandardScaler()),
         ('elasticnet', ElasticNet())]
# Create the pipeline: pipeline 
pipeline = Pipeline(steps)
# Specify the hyperparameter space
parameters = {'elasticnet__l1_ratio':np.linspace(0,1,30)}
# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, random_state=42)
# Create the GridSearchCV object: gm_cv
gm_cv = GridSearchCV(pipeline, param_grid = parameters, cv=3)
# Fit to the training set
gm_cv.fit(X_train, y_train)
# Compute and print the metrics
r2 = gm_cv.score(X_test, y_test)
print("Tuned ElasticNet Alpha: {}".format(gm_cv.best_params_))
print("Tuned ElasticNet R squared: {}".format(r2))


# In[ ]:


# Course Recap:
'''
1. use machine learning techniques to build predictive models
(classification, regression)./ with real-world data
2. Ubderfitting and overfitting
3. Test-train split
4. Corss-validation
5. Grid search
6. lasso/ ridge regression
7. pre-processing
8. For more: Check out the scikit-learn documentation / 
   O'Reilly, Introduction to Machine Learning with Python 
'''

