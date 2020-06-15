library()
df3 = mtcars
summary(df3)
str(df3)


df3$am = factor(df3$am)
str(df3)
df3$vs = factor(df3$vs)
str(df3)

#basic plot
boxplot(mpg~am, data=df3)
#ggplot2
library(ggplot2)
ggplot(data=df3,aes(x=am,y=mpg))+geom_boxplot()
#linear regression
#scale numeric features

numeric_features = c('cyl','disp','hp',
                     'drat','wt','qsec','gear','carb')
df3[numeric_features]=scale(df3[numeric_features])
lr1=lm(mpg~hp, data=df3)
summary(lr1)
plot(df3$hp,df3$mpg)
abline(lr1,col='red')
lr2=lm(mpg~., data=df3)
summary(lr2)
#Eliminate irrelevant variables
step(lr2, direction = 'backward')
lr2_update = lm(mpg~wt+qsec+am, data=df3)
summary(lr2_update)
