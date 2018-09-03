
# coding: utf-8

# In[9]:


# How good is your model? (video recap)
'''
1. Classification metrics
   Mearsuring model performance with accuarcy:
   Fraction of correctly classified samples
   Not always a useful metric
2. Spam classification: 99% of emails are real; 1% of emails are spam
   Therefore, classification on spam is bad, > 99% accuaracy, 
   fails at its original purpose
   solution: classification imbalance, need more nuanced metrics
3. Diagnosing classification predictions:
   Confusion matrix > True Positive(tp), True Negative(tn), 
                      False Postive(fp), False Negative (fn)
   *Accuracy = (tp + tn) / (tp + tn + fp + fn)
   *Precision = tp / (tp + fp) ; also called positive predictive value of PPV
   *Recall = tp / (tp + fn) ; also called sensitivity, hit rate, or true positive rate
   *F1 score = 2*(precision * recall) / (precision + recall); it is the harmonic mean of precision and recall
   High precision: Not many real emails predicted as spam
   High recall: Predicted most spam eamils correctly
'''
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
knn = KNeighborsClassifier(n_neighbors = 8)
X_trian, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, random_state=42)
knn.fit(X_trian, y_train)
y_pred = knn.predict(X_test)
print (confusion_matrix(y_test, y_pred))
print (classification_report(y_test, y_pred))


# In[ ]:


# Logistic regression and ROC curve (video recap)
'''
Logistic regression(log reg) is used in classification problems, 
not regression problems.

Log reg for binary classification:
When we have 2 possibile labels for the target variable. Given one feature, 
log reg will output a probability(p) with respect to the target variable.
If p > 0.5, we label the data as '1'; if p < 0.5, we label it '0'.
Note that log reg produces a linear decision boundary, using log reg in 
scikit-learn follows exactly the same formula that you know.
'''
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# Instatiate the classifier
logreg = LogisticRegression()
# Split your data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    test_size=0.4, random_state=42)
# Fit the model on your training data
logreg.fit(X_train, y_train)
# Predict on your test set
y_pred = logreg.predict(X_test)

'''
Notice that in defining log reg, we have specified a threshold of 0.5 for the 
probability, a threshold that defines our model. (By default, log reg threshold=0.5)
The concept of threshold is not specific to log reg. For example: k-NN classifiers 
also have thresholds.

What happens if we vary the threshold? 
What happens to the true positive and false positive rates as we vary the threshold?
The set of points we get when trying all possible thresholds is called the 
"Receiver Operating Characteristic" curve (ROC curve).
'''
# To plot the ROC curve
# Import module
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
y_pred_prob = logreg.repdict_proba(X_test)[:,1]
# Call the function
fpr,tpr,thresholds = roc_curve(y_test, y_pred_prob)
'''
We unpacked the result into three variables: false positive rate (fpr),
true positive rate (tpr), and the thresholds
Plot the fpr and tpr using pyplot's plot function to produce a figure
'''
plt.plot([0,1],[0,1],'k--')
plt.plot(fpr,tpr,label='Logistic Regression')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Logistic Regression ROC curve')
plt.show()
'''
Predicted probabilities of the model assigning a value of '1' to the 
observation in question. This is because to compute the ROC we do not merely want
the predictions on the test set, but we want the probability that our log reg model 
outputs before using a threshold to predict the label.
To do this, we apply the method predict proba to the model and pass it the test data.
predict proba returns two columns: each column contains the probabilities for the 
respective target values. We choose the second columnm the one with index 1, 
that is, the probabilities of the predicted labels being '1'.
"y_pred_prob = logreg.repdict_proba(X_test)[:,1]"
'''

#Area under the ROC curve (video recap)
'''
Question: given the ROC curve, can we extract a metric of interest?
# Area under the ROC curve(AUC)
Larger area under the ROC curve = better model (ideal is precision=1, the most top
left spot in the graph)
AUC is a popular metric for classification models
'''
from sklearn.metrics import roc_auc_score
#instantiate classifier, split data, fit the model to training data set
logreg = LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, 
                                                    random_state=42)
logreg.fit(X_train, y_train)
# compute the predicted probabilities
y_pred_prob = logreg.predict_proba(X_test)[:,1]
# pass the true labels and the predicted probabilities to roc auc score
roc_auc_score(y_test,y_pred_prob)
# print AUC score
print ("AUC: {}".format(roc_auc_score(y_test, y_pred_prob)))
# AUC using cross-validation
from sklearn.model_selection import cross_val_score
# Passing it the estimator, the features, and the target
# additionally pass it the keyword argument scoring equals "roc auc"
cv_scores = cross_val_score(logreg, X, y, cv=5,scoring='roc_auc')
print ("AUC scores computed using 5-fold cross-validation: {}".format(cv_scores))


# In[12]:


# Hyperparameter tuning (video recap)
'''
1. Linear regression: Choosing parameters
2. Ridge/lasso regression: Choosing alpha
3. k-Nearest Neighbors: Choosing n_neighbors

Parameters like alpha and k : Hyperparameters
Hyperparameters cannot be learned by fitting the model
Fundamental key for building a successful model: choosing the correct hyperparameter

How to choose the correct hyperparameter
#1 Try a bunch of different hyperparameter values
#2 Fit all of them seperately
#3 See how well each performs
#4 Choose the best performing one
* It is essentail to use cross-validation

Grid search cross-validation
" We choose a grid of possibile values we want to try 
for the hyperparameter or hyperparameters."
For example: we have two hyperparameters x and y. We use 'grid search' to see k-fold
cross-validation that which grid perform the best. 
In scikit-learn, it called "GridSearchCV"
'''
from sklearn.model_selection import GridSearchCV
import numpy as np
# Specify the hyperparameter as dictionary, key=hyperparameter name
# Setup the hyperparameter grid, param_grid
param_grid = {'n_neighbors':np.arange(1,50)}
knn = KNeighborsClassifier()
# use GridSearchCV and pass the model
knn_cv = GridSearchCV(knn, param_grid, cv=5)
knn_cv.fit(X,y)
knn_cv.best_params_
print (knn_cv.best_params_)
print (knn_cv.best_score_)


# In[ ]:


# Hyperparameter tuning with RandomizedSearchCV
'''
GridSearchCV can sometimes be very expensive to perform. Therefore, you can 
consider to use RandomizedSearchCV (not trying all the hyperparameter)
'''
# Import necessary modules
from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV

# Setup the parameters and distributions to sample from: param_dist
param_dist = {"max_depth": [3, None],
              "max_features": randint(1, 9),
              "min_samples_leaf": randint(1, 9),
              "criterion": ["gini", "entropy"]}

# Instantiate a Decision Tree classifier: tree
tree = DecisionTreeClassifier()

# Instantiate the RandomizedSearchCV object: tree_cv
tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)

# Fit it to the data
tree_cv.fit(X,y)

# Print the tuned parameters and score
print("Tuned Decision Tree Parameters: {}".format(tree_cv.best_params_))
print("Best score is {}".format(tree_cv.best_score_))


# In[ ]:


# Hold-out set for final evaluation (video recap)
'''
Topic: Report how well my model can perform on a never-seen-before dataset.

> Therefore, I want to use my model to predict on some labeled data,
  compare my prediction to the actual labels, and compute the scoring function.
> However, using all data for cross-validation is not ideal. 
  #1 Split data into training and hold-out set at the begining.
  #2 Perform grid search cross-validation on training set.
  #3 Choose best hyperparameters and evaluate on hold-out set
'''
# Hold-out set in practice I: Classification
# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
# Create the hyperparameter grid
c_space = np.logspace(-5, 8, 15)
param_grid = {"C":c_space, 'penalty': ['l1', 'l2']}
# Instantiate the logistic regression classifier: logreg
logreg = LogisticRegression()
# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.4, 
                                                    random_state = 42)
# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg,param_grid,cv=5)
# Fit it to the training data
logreg_cv.fit(X_train,y_train)
# Print the optimal parameters and best score
print("Tuned Logistic Regression Parameter: {}".format(logreg_cv.best_params_))
print("Tuned Logistic Regression Accuracy: {}".format(logreg_cv.best_score_))


# Hold-out set in practice II: Regression
# Import necessary modules
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.4, random_state=42)
# Create the hyperparameter grid
l1_space = np.linspace(0, 1, 30)
param_grid = {'l1_ratio': l1_space}
# Instantiate the ElasticNet regressor: elastic_net
elastic_net = ElasticNet()
# Setup the GridSearchCV object: gm_cv
gm_cv = GridSearchCV(elastic_net, param_grid, cv=5)
# Fit it to the training data
gm_cv.fit(X_train, y_train)
# Predict on the test set and compute metrics
y_pred = gm_cv.predict(X_test)
r2 = gm_cv.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
print("Tuned ElasticNet l1 ratio: {}".format(gm_cv.best_params_))
print("Tuned ElasticNet R squared: {}".format(r2))
print("Tuned ElasticNet MSE: {}".format(mse))

