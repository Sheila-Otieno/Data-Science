library(dplyr)
library(ggplot2)
data <- read.csv("data1.csv")
head(data)
summary(data)
str(data)
#Find which "Invoice.ID" has the highest "TotalPrice"
#use the which.max method to get the highest price
data$Invoice.ID[which.max(data$TotalPrice)]

#Calculate average "Rating" by different "Customer.type"
#aggregate function 
avg_rating = aggregate(x= data$Rating, by = list(data$Customer.type), 
          FUN = mean)
print(avg_rating)

#How many Fashion accessories products have been sold in January
#summarize function
data %>% group_by(data$Month.in.date =="Jan") %>%
  summarize(product= sum(Product.type == "Fashion accessories"))

#Use the pie chart to show how many products have been sold
ggplot(data, aes(x="", y=Quantity, fill=Product.type)) +
  geom_bar(stat="identity", width=1, color="white") +
  coord_polar("y", start=0)+theme_void()

#Use the barchart to show "TotalPrice" grouping by "City" and "Product.type"
ggplot(data, aes(fill=Product.type, y=City, x=TotalPrice)) + 
  geom_bar(position="fill", stat="identity")
#Choose one model to predict "Gross.income". Show your prediction error
#select the variables to use for the prediction
data2 <- data%>% select(Quantity,TotalPrice,Rating,Gross.income)
#check for any null values
check_na = function(x){any(is.na(x))} 
apply(data2, 2, check_na)
#split the data into training and test set
data2[,1:3] = scale(data2[,1:3])
training.id = sample(nrow(data2), round(nrow(data2)*0.8))
TrainSet = data2[training.id,]
TestSet = data2[-training.id,]
#Decision tree
#DT
library(rpart)
dt.fit = rpart(Gross.income~., data = TrainSet, method = "class")
pred.dt = predict(dt.fit, newdata = TestSet[,1:3], type = "class")
table(TestSet[,4], pred.dt)
library(rpart.plot)
rpart.plot(dt.fit)

