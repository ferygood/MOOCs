
# coding: utf-8

# In[3]:


# Statistical Thinking in Python (Part1) 
#1 Graphical exploratory data analysis
# Introduction to exploratory data analysis (video recap)
'''
Exploratory data analysis (EDA)
The process of organizing, plotting, and summarizing a data set.

'Exploratory data analysis can never be the whole story, but nothing else
can serve as the foundation stone' - John Tukey

2008 US swing state election results (open with pandas)
taking data from tabular form, DataFrame and representing it graphically.
'''
import pandas as pd
df_swing = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Statistical Thinking in Python/2008_swing_states.csv')
print (df_swing[['state', 'county', 'dem_share']])

# Plotting a histogram (video recap)
import matplotlib.pyplot as plt
# _ is a dummy variable in python 
# dummy variable is to prevent unnecessary output from being displayed
_ = plt.hist(df_swing['dem_share'])
_ = plt.xlabel('percent of vote for Obama')
_ = plt.ylabel('number of counties')
plt.show()
# Always label your axis!!
# Histograms with differnet binning
# Setting the bins of a histogram
bin_edges = [0,10,20,30,40,50,60,70,80,90,100]
_ = plt.hist(df_swing['dem_share'], bins=bin_edges)
plt.show()
'''
Seaborn (Speaker recommend)
An excellent Matplotlib-based statistical data visualization package
written by Michael Waskom.
'''
import seaborn as sns
sns.set() # Getting seaborn default setting
_ = plt.hist(df_swing['dem_share'])
_ = plt.xlabel('percent of vote for Obama')
_ = plt.ylabel('number of counties')
plt.show()

'''
The square root rule
It is a commonly-used rule of thumb for choosing number of bins:
Choose the number of bins to be the square root of the number of samples.
numpy.sqrt()
'''

#Plotting all of your data: Bee swarm plots (video recap)
'''
<Binning bias>
The same data may be interpreted differently depending on choice of bins.
One of the solution is to use Bee swarm plot.
<Bee swarm plot>
Requirement: data is a well-organized pandas dataframe (each column is feature and 
each row is observation)
'''
#Generating a bee swarm plot
_ = sns.swarmplot(x='state', y='dem_share', data=df_swing)
_ = plt.xlabel('state')
_ = plt.ylabel('percent of vote for Obama')
plt.show()  #2008 US swing state election results


# Plot all of your data: ECDFs (video recap)
'''
<Empirical cumulative distribution function (ECDF)>
When we want to classify our data to two group, and the number of data is too big
that can not interpret by bee swarm plot. We can considerate to use ECDFs.
Advatages: can plot all data and see the distribution
'''
import numpy as np
x = np.sort(df_swing['dem_share'])
y = np.arange(1, len(x)+1) / len(x)
_ = plt.plot(x, y, marker = '.', linestyle = 'none')
_ = plt.xlabel('percent of vote for Obama')
_ = plt.ylabel('ECDF')
plt.margins(0.02) # keeps data off plot edges, give us buffer all around the plot
plt.show()

# An example of three line in one ECDF
# Compute ECDFs
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)
# Plot all ECDFs on the same plot
_ = plt.plot(x_set,y_set, marker='#', linestyle='none')
_ = plt.plot(x_vers,y_vers, marker='*', linestyle='none')
_ = plt.plot(x_virg,y_virg, marker='+', linestyle='none')
# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')
# Display the plot
plt.show()

# Onward toward the whole story! (video recap)
'''
Thinking probabilistically
Discrete and continuous distributions
The power of hacker statisitcs using np.random()
'''


# In[13]:


# Introduction to summary statistics: The sample mean and median (video recap)
'''
In this part, you will learned how to graphically explore data, compute useful
summary statistics, which serve to concisely describe salient features of data
set with a few numbers.

Mean is eaily be affected by outliers.
The middle value of a data set >> The median

'''
import numpy as np
import pandas as pd

df_swing = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Statistical Thinking in Python/2008_swing_states.csv')
mean_dem_share = np.mean(df_swing['dem_share'])
print (mean_dem_share)

median_dem_share = np.median(df_swing['dem_share'])
print (median_dem_share)

# Video time (Percentiles, Outliers, and box plots)
'''
50 percentile = median (50% of the data is less than the median)
np.percentile()
IQR = interquartile range (25-75 percentile)
wisker = 1.5 IQR or extent of data
Normally, outlier is defined as larger or less than 2 IQR
'''

percentile_dem_share = np.percentile(df_swing['dem_share'],[25,50,75])
print (percentile_dem_share)
#array([37.3025 43.185  49.925])

#Generating a Bioxplot by using seaborn
import matplotlib.pyplot as plt
import seaborn as sns
df_all_states = pd.read_csv('D:/R316yao/My_Git/Python/DataCamp/Statistical Thinking in Python/2008_all_states.csv')

_ = sns.boxplot(x='east_west',y='dem_share',data=df_all_states)
_ = plt.xlabel('region')
_ = plt.ylabel('percent of vote for Obama')
plt.show()


#Video time (Variance and standard deviation)
'''
Variance:
The mean squared distance of the data from their mean
Informally, a measure of the spread of data.
np.var()

Standard Deviation:
the square root of variance
np.std()
'''
#Video time(Covariance and the Pearson correlation coefficient)
'''
Generating a scatter plot
Covariance:
A measure of how two quantities vary together
np.cov()


Pearson correlation coefficient
p = Pearson correlation = covariance/ (std of x)(std of y), 
means variability due to codependence/ independent variability

'''
_ = plt.plot(total_votes/1000, dem_share, marker='.', linestyle='none')
_ = plt.xlabel('total votes (thousands)')
_ = plt.ylabel('percent of vote for Obama')


# In[4]:


#Video time (Probabilistic logic and statistical inference)
'''
What is the goal if statistical inference?
1. To draw probabilistic conclusions about what we might expect if we collected 
   the same data again.
2. To draw actionable conclusions from data.
3. To draw more general conclusions from relatively few data or observations.

Why do we use the language of probability?
Which of the following is 'not' a reason why we use probabilistic language in
statistical inference?
1. Probability provides a measure of uncertainty
2. Probabilistic language is not very percise.
3. Data are almost never exactly the same when acquired again, and probability 
   allows us to say how much we expect them to vary.
'''
#Video time (Random number generators and hacker statisitcs)
'''
Hacker statistics
Use simulated repeatd measurements to compute probabilities.
Blaise Pascal (Coin Flips)
======
The np.random module
Suite of functions based on random number generation

np.random.random():
draw a number between 0 and 1
Bernoulli trial = An experiment that has two options, 
"success" (True) and "failure" (False).

Random number seed
Integer fed into random number generating algorithm
Manually seed random number generator if you need reproducibility
Specified using np.random.seed()
'''
# Simulating 4 coin flips
import numpy as np
np.random.seed(42)
random_numbers = np.random.random(size=4)
print (random_numbers)
#array([0.37454012 0.95071431 0.73199394 0.59865848])
heads = random_numbers < 0.5
print (heads)
#array([ True False False False], dtype=bool)
print (np.sum(heads))
#1

n_all_heads = 0 # Initialize number of 4-heads trials
for _ in range(10000):
    heads = np.random.random(size=4)<0.5
    n_heads = np.sum(heads)
    if n_heads == 4:
        n_all_heads += 1
print (n_all_heads / 10000)
# 0.0621



#The np.random module and Bernoulli trials
import matplotlib.pyplot as plt
def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0
    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()
        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success

# Seed random number generator
np.random.seed(42)
# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)
# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100,0.05)
# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults, normed=True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')
# Show the plot
plt.show()

#Video time(Probability distributions and stories: The Binomial distribution)
'''
Probability mass function(PMF):
The set of probabilities of discrete outcomes

Discrete Uniform PMF

Probability distribution: A mathematical description of outcomes.

Binomial distribution: the story:
The number r of successes in n Bernoulli trials with probability p of success,
is Binomially distributed.
The number r of heads in 4 coins flips with probability 0.5 of heads, is 
Binomially distributed.
'''
# Sampling from the Binomial distribution
np.random.binomial(4,0.5) #4 times, flip coin prob 0.5
np.random.binomial(4,0.5, size=10) #repeat 10 times
#The Binomial PMF
samples = np.random.binomial(60,0.1,size=10000)

# Video time (Poisson processes and the Poisson distribution)
'''
Poisson process:
The timming of the next event is completely independent of when the previous
event happend.
Example of Poisson processes:
Natural births in a given hospital, Hit on a website during a given hour, 
Meteor strikes, molecular collisions in a gas, aviation incidents, Buses in
Poissonville

Poisson distribution:
The number r of arrivals of a Poisson process in a given time interval with
average rate of λ arrivals per interval is Poisson distributed.
The number r of hits on a website in one hour with an average hit rate of 
6 hits per hour is Poisson distributed.
# Limit of the Binomial distribution for low probability of success and large
number of trials. That is, for rare events.
'''
#The Poisson CDF
samples = np.random.poisson(6, size=10000)
x, y =ecdf(samples)
_ = plt.plot(x,y, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('number of successes')
_ = plt.ylabel('CDF')

plt.show()

'''
When we have rare events (low p, high n), the Binomial distribution is Poisson.
This has a single parameter, the mean number of successes per time interval, in our
case the mean number of no-hitters per season.
''''
# Draw 10,000 samples out of Poisson distribution: n_nohitters
n_nohitters = np.random.poisson(251/115, size=10000)
# Compute number of samples that are seven or greater: n_large
n_large = np.sum(n_nohitters >= 7)
# Compute probability of getting seven or more: p_large
p_large = n_large/10000
# Print the result
print('Probability of seven or more no-hitters:', p_large)



# In[1]:


#Part4
#Video time(Probability density functions)
'''
Continue distribution
PDF (Probability density functions)
probability = area under the PDF
'''
'''
Introduction to the Normal distribution
Mean,
Std=how wide, how seperate
Caution: the mean and std of Normal distribution are not same as the 
calculated from data.
'''
# Draw 100000 samples from Normal distribution with stds of interest: samples_std1, samples_std3, samples_std10
samples_std1 = np.random.normal(20,1,size=100000)
samples_std3 = np.random.normal(20,3,size=100000)
samples_std10 = np.random.normal(20,10, size=100000)
# Make histograms
_ = plt.hist(samples_std1,bins=100,normed=True, histtype='step')
_ = plt.hist(samples_std3, bins=100, normed=True, histtype='step')
_ = plt.hist(samples_std10, bins=100, normed=True, histtype='step')
# Make a legend, set limits and show plot
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.50)

plt.show()


'''
The Normal distribution:
Properties and warnings
The Gaussian distribution = The Normal distribution
'''

'''
The Exponential distribution
The waiting time between arrivals of a Poisson process is Exponentially distributed
# Nuclear incidents:
  Timing of one is independent of all others
'''
# Exponential inter-incident times
mean = np.mean(inter_times)
samples = np.random.exponential(mean, size=10000)
x,y = ecdf(inter_times)
x_theor, y_theor = ecdf(samples)
_ = plt.plot(x_theor, y_theor)
_ = plt.plot(x,y, marker='.', linestyle='none')
_ = plt.xlabel('time(days)')
_ = plt.ylabel('CDF')
plt.show()

'''
#1 Matching a story and a distribution
How might we expect the time between Major League no-hitters to be distributed?
Be careful here: a few exercises ago, we considered the probability distribution 
for the number of no-hitters in a season. Now, we are looking at the probability 
distribution of the time between no hitters.
Ans: Exponential

#2 Waiting for the next Secretariat
Unfortunately, Justin was not alive when Secretariat ran the Belmont in 1973.
Do you think he will get to see a performance like that? To answer this, you are 
interested in how many years you would expect to wait until you see another 
performance like Secretariat's. How is the waiting time until the next performance
as good or better than Seretariat's distributed?
Choose the best answer.
Ans:Exponential, A horse as fast as Secretariat is a rare event, which can be 
modeled as a Poisson process, and the waiting time between arrivals of a Poisson
process is Exponentially distributed.
'''

