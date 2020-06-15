library()
x1 = seq(2020001,2020100)
x2 = runif(100,min=80,max=100)
x3 = rnorm(100,mean=80,sd=7)
x4 = rpois(100,lambda=70)

df=data.frame(x1,x2,x3,x4)
names(df) = c('StudentID','DataMining','Statistics','BDP')
#mean of each column
apply(df[,2:4],2,mean)
#student with the highest score in each course
df$StudentID[which.max(df(c['DataMining']))]
#student with highest score
df$StudentID[which.max(apply(df[,2:4],1,sum))]
             