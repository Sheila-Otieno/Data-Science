vehicles <- read.csv(unz("vehicles.csv.zip", "vehicles.csv"),stringsAsFactors = F)
head(vehicles)
labels <- do.call(rbind, strsplit(readLines("varlabels.txt")," - "))
#labels <- read.table("varlabels.txt",sep = "-",header=FALSE)
head(labels)
labels <- read.table("varlabels.txt",sep = ",",header=FALSE)
head(labels)
nrow(vehicles)
ncol(vehicles)
names(vehicles)
length(unique(vehicles[,"year"]))
which.max(vehicles$year)
head(vehicles$year)
min(vehicles[,"year"])
max(vehicles[,"year"])

#aggregation
vehicles$trany[vehicles$trany == ""]<-NA
#create column to store auto and manual based cars
vehicles$trany2 <-ifelse(substr(vehicles$trany, 1, 4) == "Auto", "Auto", "Manual")
vehicles$trany2 <- as.factor(vehicles$trany2)
table(vehicles$trany2)
library(plyr)
#analyze fuel efficiency per year
mpgByYr <- ddply( vehicles, ~year, summarise, avgMPG = mean(comb08), avgHghy = mean(highway08), avgCity = mean(city08) )
library(ggplot2)
ggplot(mpgByYr, aes(year, avgMPG)) + geom_point() + geom_smooth() + xlab("Year") + ylab("Average MPG") + ggtitle("All cars")

#subset()
gasCars <- subset(vehicles,fuelType1 %in% c("Regular Gasoline", "Premium Gasoline", "Midgrade Gasoline") & fuelType2 == "" & atvType != "Hybrid") 
#aggregation of mpg over the years
mpgByYr <- ddply( gasCars, ~year, summarise, avgMPG = mean(comb08), avgHghy = mean(highway08), avgCity = mean(city08) )
#ggplot
ggplot(mpgByYr, aes(year, avgMPG)) + geom_point() + geom_smooth() + xlab("Year") + ylab("Average MPG") + ggtitle("Gas cars")
