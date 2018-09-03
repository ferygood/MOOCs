#video highlight, useful functions
#Loads of useful functions, sapply(), vapply(), lapply()
#sort(), print(), identical()

v1 <- c(1.1,-7.1,5.4,-2.7)
v2 <- c(-3.6,4.1,5.8,-8.0)
mean(c(sum(round(abs(v1)))), sum(round(abs(v2))))
#abs(), absolute number 絕對值
abs(c(1.1,-7.1,5.4,-2.7))
abs(c(-3.6,4.1,5.8,-8.0))
#round(), round function 四捨五入
round(c(1.1,-7.1,5.4,-2.7))
#sum(), calculate the sum 算總和
sum(c(1,7,5,3))
#mean() calculate the arithmetic mean 算平均
mean(c(16,22))

#functions for data structures
#log=logical,ch=character string, seq=generate a sequence form start to end with increments
#rep = replicate input, sort=sorting number by descending number 
li <- list(log=TRUE, ch='hello', int_vec = sort(rep(seq(8,2,by=-2), times=2)))
str(li)
#R expression, is.*(), as.*()
is.list(li)
is.list(c(1,2,3))
li2 <- as.list(c(1,2,3))
is.list(li2)
unlist(li)
#append(), rev()
str(rev(li))  #reverse
str(append(li, rev(li))) #one after another, append


#Regular Expressions
#Sequence of (meta)characters, Pattern existence, Pattern replacement, Pattern extraction, grep(), grepl(), sub(), gsub()
animals <- c("cat","moose", "impala", "ant", "kiwi")
#grepl(pattern = <regex>, x= <stinrg>)
#want to find animals name has 'a'
grepl(pattern='a', x=animals)
grep(pattern='a', x=animals)
which(grepl(pattern = 'a',x=animals))
#name begins with a
grepl(pattern='^a', x=animals)
grep(pattern = '^a', x=animals)
#name ends with a
grepl(pattern='$a', x=animals)
grep(pattern='$a', x=animals)
#sub(), gsub()
#sub(pattern = <regex>, replacement=<str>,x=<str>)
sub(pattern='a', replacement = "o", x=animals)
gsub(pattern='a', replacement = "o", x=animals)
gsub(pattern = 'a|i', replacement ='_', x=animals)


#Times and Dates
today <- Sys.Date()
today
class(today)
now <- Sys.time()
now
class(now)
#Create Date objects
my_date <- as.Date("1971-05-14")
my_date
class(my_date)
#Create POSIXct objects
my_time <- as.POSIXct("1971-05-14 11:25:15")
my_time
#Date arithmetic
my_date + 1 #days incremented by 1
my_date2 <- as.Date("1998-09-29")
my_date2
my_date2 - my_date
#POSIXct arithmetic
my_time
my_time + 1 #seconds incremented by 1
my_time2 <- as.POSIXct("1974-07-14 21:11:55 CET")
my_time2 - my_time
#Under the hood...
my_date
unclass(my_date)  #498 days from January 1, 1970
my_time
unclass(my_time)
#following R commands will all create the same Date object for the 13th day in January of 1982
as.Date("1982-01-13")
as.Date("Jan-13-82", format="%b-%d-%y")
as.Date("13 January, 1982", format = "%d &B, %Y")
#Dedicated R packages: lubridate, zoo, xts
