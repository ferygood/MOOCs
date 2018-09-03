#laapyl video highlight
nyc <- list(pop=8405837,
            boroughs = c('Manhattan', 'Bronx', 'Brooklyn',
                         'Queens', 'Staten Island'),
            capital = FALSE)
for (info in nyc) {
  print(class(info))
}
#using lapply to make it easier!
lapply(nyc,class)


#another example, nchar=number of characters
cities <- c('New York', 'Paris','London','Tokyo','Rio de Janeiro','Cape Town')
num_chars <- c()
for (i in 1:length(cities)) {
  num_chars[i] <- nchar(cities[i])
}
#or you can use lapply
lapply(cities, nchar)
#turn a list to a vector
unlist(lapply(cities,nchar))


#example
oil_prices <- list(2.37, 2.49, 2.18, 2.22, 2.47, 2.32)
triple <- function(x) {
  3*x
}
result <- lapply(oil_prices, triple)
str(result)
unlist(result)
#another case, change triple to multiple
oil_prices <- list(2.37, 2.49, 2.18, 2.22, 2.47, 2.32)
multiply <- function(x, factor) {
  x * factor
}
# factor=4
times4 <- lapply(oil_prices, multiply, factor=4)
unlist(times4)
str(times4)


#Named function
triple <- function(x) {3*x}
#anonymous functions
function(x) {3*x}
#use anonymous function inside lapplay()
lapply(list(1,2,3), function(x){3*x})


#sapply video highlight
# review lapply: 
#(1) apply function over list or vector 
#(2) Function can return R objects of different classes
#(3) List necessary to store heterogeneous content
cities <- c('New York', 'Paris','London','Tokyo','Rio de Janeiro','Cape Town')
unlist(lapply(cities,nchar))
sapply(cities,nchar)
sapply(cities,nchar,USE.NAMES = FALSE)  #USE.NAMES=TRUE by default
#first and last letter example
first_and_last <- function(name){
  name <- gsub(' ','',name) 
  letters<-strsplit(name, split='')[[1]]
  c(first=min(letters), last=max(letters))
  }
first_and_last('New York')
sapply(cities, first_and_last)
# Simply case
unique_letters <- function(name){
  name <- gsub(" ","",name)
  letters <- strsplit(name, split='')[[1]]
  unique(letters)
}
unique_letters("London")
lapply(cities, unique_letters)
sapply(cities, unique_letters)


#vapply video highlight
#Recap: lapply(), apply function over list or vector, output=list
#sapply(), apply function over list or vector. Try to simplyfy list to array
#vapply(), apply function over list or vector explicity specify output format
#In some case, vapply is similar to sapply
cities <- c('New York', 'Paris','London','Tokyo','Rio de Janeiro','Cape Town')
sapply(cities, nchar)
vapply(cities, nchar, numeric(1))

