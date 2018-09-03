#7/15 factor
#factor, level, summary
#continuous or categoritcal variable
yuyuhakushuo = 'a Japanese manga'
#factor()
gender_vector <- c('boy','girl','girl','boy','girl')
factor_gender_vector <- factor(gender_vector)
factor_gender_vector

#nominal categorical variable, ordinal categorical variable
#levels(), summary()
levels(factor_gender_vector) <- c('Male','Female') #choose the first one(boy) as male
factor_gender_vector
summary(gender_vector)
summary(factor_gender_vector)
Male <- factor_gender_vector[1]
Female <- factor_gender_vector[2]
Male
Female

#orderd factors
speed_vector <- c('medium','slow','slow','medium','fast')
factor_speed_vector <- factor(speed_vector, ordered=TRUE, 
                              levels=c('slow','medium','fast'))
factor_speed_vector
summary(factor_speed_vector)
da2 <- factor_speed_vector[2]
da5 <- factor_speed_vector[5]
da2 > da5   #Is data analyst 2 faster than data analyst 5?

