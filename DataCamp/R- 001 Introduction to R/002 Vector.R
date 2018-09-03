# 7/14 R training
# Vectors
Tom_score_vector <- c(98,50,60,70)
Sam_score_vector <- c(95,88,70,40)
subject_names_vector <- c('Math',"Science","Chemistry",'Informatics')

#names is for the same label, has to be name
names(Tom_score_vector) <- subject_names_vector
names(Sam_score_vector) <- subject_names_vector

table <- Tom_score_vector + Sam_score_vector
table

#calculate total score
total_Tom <- sum(Tom_score_vector)
total_Sam <- sum(Sam_score_vector)
total_Tom
total_Sam
total_Tom > total_Sam

# R start from 1 not 0
Tom_score_vector[1]
Sam_score_vector[4]

#remeber to add combine c() for select multiple data
Tom_score_vector[c(1,3,4)]
Tom_score_vector[c(2:4)]
Tom_score_vector[c('Informatics','Math')]

averge_Tom <- mean(Tom_score_vector)
averge_Tom

#Comparison, return a logical
selection_vector <- Tom_score_vector > 85
selection_vector

Tom_good_at <- Tom_score_vector[selection_vector]
Tom_good_at
