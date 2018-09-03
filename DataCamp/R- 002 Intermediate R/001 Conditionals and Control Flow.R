#Relational Operator
#Equality ==, Inequailty !=
TRUE == TRUE
TRUE == FALSE
3 != 2
3 > 5
5 > 1 
'hello' > 'goodbye'     # alphabetical Order
TRUE < FALSE            # true = 1 , false = 0

#compare vectors
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)
linkedin > 15
linkedin <= 5
linkedin > facebook

#compare matrices
views <- matrix(c(linkedin, facebook), nrow=2, byrow=TRUE)  
views == 13       #When does views equal 13
views <= 14       #When is views less than or equal to 14

#Logical Operators, and &, or |, not !
c(TRUE,TRUE,FALSE) & c(TRUE,FALSE,FALSE)
c(TRUE,TRUE,FALSE) && c(TRUE,FALSE,FALSE)  #only represent the first element
last <- tail(linkedin, 1)
last < 5 | last > 10
last > 15 & last <= 20

#pop quiz
x <- 5
y <- 7
!(!(x < 4) & !!!(y > 12))  #what will it return? TRUE or FALSE

#Blend it all together
#Select the second column, named day2, from li_df: second
second <- li_df$day2
#Build a logical vctor, TRUE if value in second is extreme: extremes
extremes <- second >25 | second<5
# Count the number of TRUEs in extremes
sum(extremes)
# Solve it with a one-liner
sum(li_df$day2 > 25 | li_df$day2 < 5)

#Conditional Statements
medium <- 'LinkedIn'
num_views <- 14
if (medium == 'LinkedIn'){print ("showing LinkedIn information")}
if (num_views > 15){print("You're popular!")}

if (medium=='LinkedIn'){print("Showing LinkedIn information")
  }else{(print("Unknown medium"))}
if (num_views>15){
  print("You're popular")
}else{print("Try to be more visible!")}

#Else if 2.0
number <- 4
if (number < 10) {
  if (number < 5) {
    result <- "extra small"
  } else {
    result <- "small"
  }
} else if (number < 100) {
  result <- "medium"
} else {
  result <- "large"
}
print(result)




