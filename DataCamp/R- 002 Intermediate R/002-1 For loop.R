#For loop
#loop over a vector
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
#two ways to iterate over vector
for (p in linkedin) {print (p)}
for (i in 1:length(linkedin)){print (linkedin[i])}

#looping over a list
nyc <- list(pop = 8405837, 
            boroughs = c("Manhattan", "Bronx", "Brooklyn", "Queens", "Staten Island"), 
            capital = FALSE)
for (p in nyc) {print(p)}
for (i in 1: length(nyc)) {print(nyc[[i]])} # iterate over list need double square brackets


#loop over matrix
ttt_raw <- c("O",NA,"X",NA,"O","O","X",NA,"X")
ttt <- matrix(ttt_raw, nrow=3, byrow=TRUE)  #ttt is a matrix of data ttt_raw
for (i in 1:nrow(ttt)) {
  for (j in 1:ncol(ttt))
    print(paste("On row", i ,"and column", j, "the board contains",ttt[i,j]))
}


#Mix it up with control flow
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
for (li in linkedin){
  if (li >10) {print("You're popular!")}
  else {print("Be more visible!")}
  print (li)

  #Next, you break it
  if (li>16){
    print("This is ridiculous, I'm outta here!")
    break
  }
  
  if (li <5) {
    print("This is too embarrasing!")
    next
  }
}


#Build a for loop from scratch
rquote <- "r's internals are irrefutably intriguing"
chars <- strsplit(rquote, split = "")[[1]]
rcount <- 0
for (char in chars) {
  if (char == "r") {
    rcount <- rcount + 1
  }
  if (char == 'u') {
    break
  }
  print (rcount)
}



