#hierarchical clustering of customers
customer = read.csv('customer.csv', header=TRUE)
str(customer)
#normalize the data by scaling
customer=scale(customer[,-1])
#hclust() method 
d <- dist(customer,method = "euclidean")
hc = hclust(d, method="ward.D2")
hc
#plot the dendogram
plot(hc, hang = -0.01, cex = 0.7)
#single method and simpler distance
hc2 = hclust(dist(customer), method="single")
#plot the dendogram
plot(hc2, hang = -0.01, cex = 0.7)
#cutting the tree into clusters
fit = cutree(hc, k = 4)
fit
table(fit)
#visualize how clusters are related in the tree
plot(hc) 
rect.hclust(hc, k = 4 , border="red")
rect.hclust(hc, k = 4 , which =2, border="red")

#kmeans clustering
# set some arbitrarily chosen seed 
set.seed(22) 
fit = kmeans(customer, 4) 
fit
#plot the clusters
plot(customer, col = fit$cluster)

#comparing three clusterings
install.packages("fpc") 
library(fpc)
#prepare three clustering(single,complete and kmeans)
single_c = hclust(dist(customer), method="single") 
hc_single = cutree(single_c, k = 4)

complete_c = hclust(dist(customer), method="complete") 
hc_complete = cutree(complete_c, k = 4)

set.seed(22) 
km = kmeans(customer, 4)

#silhouette WSS
cs = cluster.stats(dist(customer), km$cluster) cs[c("within.cluster.ss","avg.silwidth")]
sapply(list(kmeans = km$cluster, hc_single = hc_single, hc_complete = hc_complete), function(c) cluster.stats(dist(customer), c)[c("within.cluster.ss","avg.silwidth")])

#trying a good kmeans
nk = 2:10 
set.seed(22)
# WSS 
WSS = sapply(nk, function(k) {kmeans(customer, centers=k)$tot.withinss }) 
WSS 
# plot it 
plot(nk, WSS, type="l", xlab= "number of k", ylab="within sum of squares")
# silhouette width 
SW = sapply(nk, function(k) { cluster.stats(dist(customer), kmeans(customer, centers=k)$cluster)$avg.silwidth}) 
SW 
# plot it
plot(nk, SW, type="l", xlab="number of clusers", ylab="average silhouette width")

