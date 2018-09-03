#Functions
#function Documentation, for example: sample()
help(sample)
?sample
args(sample)

#use a function
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)
# Calculate average number of views
avg_li <- mean(linkedin)
print (avg_li)
# Inspect avg_li and avg_fb
avg_fb <- mean(facebook)
print (avg_fb)
# Calculate the mean of the sum
avg_sum <- mean(linkedin+facebook)
# Calculate the trimmed mean of the sum
avg_sum_trimmed <- mean(linkedin+facebook,trim=0.2)
# Inspect both new variables
print (avg_sum)
print (avg_sum_trimmed)


# The linkedin and facebook vectors have already been created for you
linkedin <- c(16, 9, 13, 5, NA, 17, 14)
facebook <- c(17, NA, 5, 16, 8, 13, 14)
# Basic average of linkedin
print (mean(linkedin))
# Advanced average of linkedin
print (mean(linkedin, na.rm = TRUE))  #na.ram remove missing value from the input vector before calculating the standard deviation


linkedin <- c(16, 9, 13, 5, NA, 17, 14)
facebook <- c(17, NA, 5, 16, 8, 13, 14)
# Calculate the mean absolute deviation
print (mean(abs(linkedin-facebook), na.rm = TRUE))  #abs, absolute differences

#20180725
#write your own function
#Create a function pow_two(): it takes one argument and returns that number squared (that number times itself)
pow_two <- function(x) {
  x^2
}
#Call this newly defined function with 12 as input
pow_two(12)
#Next create a function sum_abs(), that takes two arguments and returns the sum of the absolute values of both arguments
sum_abs <- function(a,b){
  abs(a) + abs(b)
}
#Finally, call the function sum_abs() with arguments -2 and -3 afterwards.
sum_abs(-2,3)

#write your own function(2)
#A random dice function
throw_die <- function(){
  number <- sample(1:6, size=1)
  number
}
throw_die()
#Define a function, hello(). It prints out "Hi there!" and returns TRUE. It has no arguments.
#Call the function hello(), without specifying arguments of course.
hello <- function(){
  print('Hi there!')
  return (TRUE)
}
hello()

#write your own function(3)
pow_three <- function(x, print_info = TRUE) {
  y <- x ^ 3
  if (print_info == TRUE){
  print(paste(x, "to the power three equals", y))  
  }
  return(y)
}
pow_three(7)
pow_three(7,TRUE)
pow_three(7,FALSE)


#20180801
#Function scoping
pow_two <- function(x) {
  y <- x^2
  return(y)
}
pow_two(4)

two_dice <- function(){
  possibilities <- 1:6
  dice1 <- sample(possibilities, size=1)
  dice2 <- sample(possibilities, size=1)
  dice1+dice2
}

#R passes arguments by value
triple <- function(x){
  x <- 3*x
  x
}
a <- 5
triple(a)
a

increment <- function(x, inc=1){
  x <- x + inc
  x
}
count <- 5
a <- increment(count, 2)
b <- increment(count)
count <- increment(count, 2)   #count is re-assigned explicitly, does the value of count change


#R you functional?
# The linkedin and facebook vectors have already been created for you
# Define the interpret function
interpret <- function(num_views) {
  if (num_views > 15) {
    print("You're popular!")
    return(num_views)
  } else {
    print("Try to be more visible!")
    return(0)
  }
}
# Call the interpret function twice
interpret(linkedin)
interpret(facebook[2])




#R you functional?(2)
# The linkedin and facebook vectors have already been created for you
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)
#The interpret() can be used inside interpret_all()
interpret <- function(num_views){
  if (num_views > 15){
    print("You're popular!")
    return(num_views)
  }else{
    print ("Try to be more visible!")
    return(0)
  }
}
# Define the interpret_all() function
# views: vector with data to interpret
# return_sum: return total number of views on popular days?
interpret_all <- function(views, return_sum=TRUE) {
  count <- 0
  for (v in views) {
    count <- count + interpret(v)
  }
  if (return_sum==TRUE){
    return (count)
  }else{
    return (NULL)
  }
}
#Call the interpret_all() function on both linkedin and facebook
interpret_all(linkedin)
interpret_all(facebook)




#R Packages
#Built-in functions
#CRAN: Comprehensive R Archive Network
#Load an R Package
#install.packages(), which as you can expect, installs a given package.
#library() which loads packages, i.e. attaches them to the search list on your R workspace
#use search() to look at the currently attached packages
search()
#qplot(mtcars$wt, mtcars$hp) to build a plot of two variables of the mtcars data frame
# Load the ggplot2 package
library(ggplot2)
# Retry the qplot() function
qplot(mtcars$wt, mtcars$hp)
# Check out the currently attached packages again
search()



#Different ways to load a package
#chunk 1
library(data.table)
require(rjson)
#chunk 2
library('data.table')
require(rjson)

