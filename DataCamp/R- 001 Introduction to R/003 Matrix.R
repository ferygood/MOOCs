#7/14 matrix
#byrow = TRUE (fill by row), byrow = FALSE (fill by column)
matrix(1:18, byrow=TRUE, nrow=3) 
matrix(1:40, byrow=FALSE, nrow=5)

#Analyze matrices
height <- c(182.1,163.2,155.0)
weight <- c(79.3,70,55)
long <- c(13,14.2,9.0)
body_status <- c(height,weight,long)
body_status
body_matrix <- matrix(body_status, byrow=TRUE, nrow=3)

colnames(body_matrix) <- c('Tom','Jerry','Granny')
rownames(body_matrix) <- c('Height','Weight','Long')
body_matrix

rowSums(body_matrix)

#oneline code to build matrix
mass <- c(41,35,89,47)
volume <- c(66,55.5,41,26)
dense <- c(2,3,6,1)
physics <- c(mass,volume,dense)
physics_matrix <- matrix(physics, byrow=TRUE, nrow = 3, dimnames = 
                           list(c('mass','volume','dense'),c('Kim','Terry','May','Athena')))
physics_matrix
rowSums(physics_matrix)
#add column
Iori <- c(50,45,4)
cbind(physics_matrix,Iori)

#add row
make <- c(123,150,133,141)
rbind(physics_matrix, make)

colSums(physics_matrix)

#select matrix elements
#first argument is row, second argument is column
physics_matrix[1,2]
physics_matrix[1,]
physics_matrix[,3]
physics_matrix[2:3,2:3]

#matrix arithmetic
physics_matrix / 5
physics_matrix + 55

