library(dplyr)
data <- read.csv("data.csv")
head(data)
summary(data)
str(data)
#check for null values
apply(data, 2, function(x) any(is.na(x)))
#Find who have the top 5 highest "serum_cholestoral". Show their IDs
data %>% 
  group_by(ID)%>%
  top_n(5,serum_cholestoral)
 
head(sort(data$serum_cholestoral, decreasing = TRUE), n=5)
#average "max_heart_rate" grouping by different "thal"
aggregate(x = data$max_heart_rate, by = list(data$thal), FUN = mean)
#boxplot to show "blood_pressure" grouping by "chest_pain_type"
library(ggplot2)
ggplot(data = data, aes(x = chest_pain_type, y = blood_pressure)) +
  geom_boxplot()
#histogram to show the distribution of age for people who have heart disease
ggplot(data, aes(x=age)) + 
  geom_histogram()
# linear dependence between "age" and "blood_pressure"


#Split dataset into training/testing 80/20 and choose one model to predict "if_heart_disease"
str(data)
data$if_heart_disease <- factor(data$if_heart_disease)
num_values <- c('blood_pressure','serum_cholestral','max_heart_rate',
                'oldpeak','number_of_major_blood_vessels')
data[num_values]= scale(data[num_values])

#classification task
#create a validation set
library(caret)
validation_df <- createDataPartition(data$if_heart_disease, p=0.8, list=F)
#split the data into 20% for validation
validation_data <- data[-validation_df,]
#80% data used for training and test
data <-data[validation_df,]
apply(data[,1:4],2,function(x){any(is.na(x))})