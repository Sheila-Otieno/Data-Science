library()
df2 = iris
summary(df2)
#calculate mean 
apply(df2[,1:4],2, mean)
#calculate mean of sepal length
apply(df2[,1:4],1,mean)
#column means
aggregate(.~Species,df2,mean)

#apply(df2[,1:4],2,function(x){apply(x.df2$Species,mean)})
plot(df2[,1:4])
library(ggplot2)
ggplot(df2, aes(Sepal.Length,Sepal.Width))+geom_point()
pairs(df2[,1:4])

#classification task
#create a validation set
library(caret)
validation_df <- createDataPartition(df2$Species, p=0.8, list=F)
#split the data into 20% for validation
validation_data <- df2[-validation_df,]
#80% data used for training and test
df2 <-df2[validation_df,]
apply(df2[,1:4],2,function(x){any(is.na(x))})
df2[,1:4]= scale(df2[,1:4])
df2 = na.omit(df2) #remove missing values
#split the 80% validation to train and test
df2_split = sort(sample(nrow(df2), nrow(df2)*.8))
train<-df2[df2_split,]
test<-df2[-df2_split,]

#random forest
library(randomForest)
rf <-randomForest(Species ~ ., data = train, ntree= 500,importance=TRUE)
rf
pred <- predict(rf,train,type="class")
table(pred, train$Species)

#decision tree
library(ISLR)
require(tree)
install.packages("rpart.plot")
library(rpart)
library(rpart.plot)
fit <- rpart(Species ~., data=train, method='class')
rpart.plot(fit, extra=106)

#KNN classification
install.packages("class")
library(class)
df2_category <-df2[df2_split,5]
knn_pred <- knn(train = train, test=test, cl=df2_category, k=3)
knn_pred
