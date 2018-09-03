#7/16 List
#Vector (one dimensional array)
#Matrices(two dimensional array)
#Data Frame(two-dimensional objects)

#Creating a list
my_vector <- 1:10
my_matrix <- matrix(1:9, ncol=3)
my_df <- mtcars[1:10,]
my_list <- list(my_vector, my_matrix, my_df)

#Creating a named list
names(my_list) <- c('vec','mat','df')
my_list

#Selecting elements from a list
#print out the vector representing the dataframe
my_list[[3]]
#print out the second element of the vector representing the dataframe
my_list[[3]][2]
#Adding more information to the list
my_list <- c(my_list, newadd = 'Tom')
my_list
str(my_list)
