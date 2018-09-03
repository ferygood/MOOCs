#Dara Frame
#print out built-in R data frame mtcars
mtcars
#head(), tail()
head(mtcars)
tail(mtcars)
#str(), str for structure in R
#appy str() is the first thing 
str(mtcars)

# Creating a data frame
name <- c("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
type <- c("Terrestrial planet", "Terrestrial planet", "Terrestrial planet", 
          "Terrestrial planet", "Gas giant", "Gas giant", "Gas giant", "Gas giant")
diameter <- c(0.382, 0.949, 1, 0.532, 11.209, 9.449, 4.007, 3.883)
rotation <- c(58.64, -243.02, 1, 1.03, 0.41, 0.43, -0.72, 0.67)
rings <- c(FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE)

# Create a data frame from the vectors
planets_df <- data.frame(name,type,diameter,rotation,rings)
planets_df
str(planets_df)   #check the structure of planets_df

#Selection of data frame elements
planets_df[1,2]
planets_df[1:3,2:4]
planets_df[1,]

#Selection of data frame elements(by variable)
planets_df[1:3,2]
planets_df[1:3,"type"]
planets_df$rings
planets_df[rings_vector,]

#Select planets with diameter < 1
subset(planets_df, subset = diameter < 1)

#Sorting
a<-c(100,10,1000)
order(a)       #output 2 1 3
a[order(a)]    #output 10 100 1000

#Sorting your dataframe
positions <- order(planets_df$diameter)
planets_df[positions,]
