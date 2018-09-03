
# coding: utf-8

# In[9]:


#Supervised Learning with scikit-learn
#Classification
#Supervised Learning video highlight
'''
The art and science of Giving computers the ability to learn to make decisions from 
data without being explicity programmed!
>EX1 Learning to predict whether an email is spam or not
>EX2 Clustering wikipedia entries into different categories
Supervised learning: Uses labeled data
Unsupervised learning: Uses unlabeled data.

*Unsupervised learning:
Uncovering hidden patterns from unlabeled data. for ex: Grouping customers into distinct 
categories (Clustering)

*Reinforcement learning:
Software agents interact with an environment. Learn how to optimize their behavior/ 
Given a system of rewards and punishments/ Draw inspiration from behavioral psychology
applications: Economics/ Genetics/ Game playing: AlphaGO

*Supervised Learning:
Predictor variables/ features and target variable
Aim: Predict the target variable, given the predictor variables
> Classification: Target variable consists of categories
> Regression: Target variable is continous
Automate time-consuming or expensive manual tasks, 
ex: Doctor's diagnosis
Make predictions about the future
ex: Will a customer click on an ad or not?
Need labeled data, ex:historical data with labels, Experiment to get labeled data,
Crowd-sourcing labeled data.

Naming conventions
Features = predictor variables = independent variables
Target variable = dependent variable = response variable

We will use scikit-learn/sklearn, integrates well with the SciPy stack.
Other libraries: TensorFlow, keras...
'''

'''
Exploratory data analysis(video), the Iris dataset, built-in scikit learn
first: getting know your data
'''
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
iris = datasets.load_iris()
print type(iris)  #sklearn.datasets.base.Bunch
print iris.keys() #dict_keys([.......])
print type(iris.data), type(iris.target) #(numpy.ndarray, numpy.ndarray)
print 'iris data shape(rows, columns): ', iris.data.shape
print iris.target_names


#Exploratory data analysis(EDA)
X = iris.data
y = iris.target
df = pd.DataFrame(X, columns = iris.feature_names)
print df.head()

#visual EDA
#df=dataframe, c=color, s=shape
pd.scatter_matrix(df, c=y, figsize=[8,8], s=150, marker='D')


# In[6]:


from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
You need to perform Exploratory data analysis(EDA) in order to understand the
structure of the data.
For a refresher on the importance of EDA, check out the first two chapters of 
"Statistical Thinking in Python"
Get started with your EDA now by exploring using pandas .head(), .info(), and
.describe() methods.
'''
df = pd.read_csv("D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)/Supervised Learning with scikit-learn/US Congressional Voting Records(1984).csv"
)
print df.head()
print df.info()
print df.describe()


# In[20]:


#Visual EDA
from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)/Supervised Learning with scikit-learn/US Congressional Voting Records(1984).csv"
)
plt.figure()
sns.countplot( x='missile',hue='party', data=df, palette='RdBu')
plt.xticks([0,1,2], ['Yes', 'No','?'])
plt.show()


# In[5]:


#The classification challenge video recap
#k-Nearest Neighbors, KNN
#Scikit-learn fit and predict. All machine learning models implemented as Python classes
#Training a model on the data = 'fiting' a model to the data, .fit() method
# To predict the labels of new data: .predict() method

#Below we sue scikit-learn to fit a classifier
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 6)
# data should be continous and in numpy or pandas dataframe
# data structure, feature in column, observation in rows
knn.fit(iris["data"], iris["target"])

#Predicting on unlabeled data
prediction = knn.predict(X_new)
X_new.shape
print 'Prediction {}'.format(prediction)


# In[11]:


'''
k-Nearest Neighbors:Fit
df = congressional voting records dataset
build your own classifier
fit a k-Nearest Neighbors classifier to the voting dataset
remember to make sure your data adheres to the format required by the scikit-learn API
feature array X, response variable y
'''
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
df = pd.read_csv("D:/R316yao/My_Git/Python/DataCamp/Machine Learing with Python (Skill Track)/Supervised Learning with scikit-learn/US Congressional Voting Records(1984).csv"
)
# Create arrays for the features and the response variable
# Note the use of .drop() to drop the target variable 'party' from the feature- 
# -array X as well as the use of the .values attribute to ensure X and y are NumPy arrays
y = df['party'].values
X = df.drop('party', axis=1).values
#create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)
#fit the classifier to the data
knn.fit(X,y)
'''
Expect output:KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
metric_params=None, n_jobs=1, n_neighbors=6, p=2,weights='uniform')
'''

#還需要將 Excel 檔案中的 no yes 轉換成布林值
# k-Nearest Neighbors:Predict
# Predict the labels for the training data X
y_pred = knn.predict(X)
# Predict and print the label for the new data point X_new
new_prediction = knn.predict(X_new)
print "Prediction: {}".format(new_prediction)
# Expected output: something like Prediction: ['     ']


# In[16]:


# Measuring model performance video
'''
In classification, accuracy is a commonly used metric
Accuracy = Fraction of correct predictions
Which data should be used to compute accuracy?
Important: How well will the model perform on new data?
1. 
Could compute accuracy on data used to fit classifier
Not indicative of ability to generalize
2. 
Split data into training and test set
fit/train the classifier on the training set
Make predictions on test set
Compare predictions with the known labels
'''
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, 
                                                    random_state=21, stratify=y)
knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print "Test set predictions:\n {}".format(y_pred)
print knn.score(X_test, y_test)




# In[18]:


'''
Model complexity
larger k = smoother decision boundary = less complex model
smaller k = more complex model = can lead to overfitting
'''
# The digits recognition dataset
# the dataset is the reduced version of MNIST in scikit-learn dataset
'''
Each sample in this scikit-learn dataset is an 8x8 image representing a handwritten 
digit. Each pixel is represented by an integer in the range 0 to 16, 
indicating varying levels of black.
'''
from sklearn import datasets
import matplotlib.pyplot as plt
#load the digits dataset: digits
digits = datasets.load_digits()
#print the keys and DESCR of the dataset
print digits.keys()
print digits.DESCR
print digits.images.shape
print digits.data.shape
#display digit #number can range from 1 to 1797
plt.imshow(digits.images[999], cmap=plt.cm.gray_r, interpolation='nearest')
print plt.show()


# In[24]:


#Train/Test Split + Fit/Predict/Accuracy
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
#Create feature and target arrays
X = digits.data
y = digits.target
# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, 
                                                    random_state = 42, stratify = y)
# Create a k=NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)
# Fit the classifier to the training data
knn.fit(X_train, y_train)
#print the accuracy
print knn.score(X_test, y_test)


# In[26]:


#Overfitting and underfitting
import numpy as np
#setup arrays to store train and test accuracies
neighbors = np.arange(1,9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))
#loop over different values of k
for i,k in enumerate(neighbors):
    #setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)
    #Fit the classifier to the training data
    knn.fit(X_train, y_train)
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)
    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)
#Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label = 'Testing Accuracy')
plt.plot(neighbors, train_accuracy, label = 'Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
print plt.show()

