Sys.setenv(JAVA_HOME='C:\\Program Files\\Java\\jre1.8.0_241')
library(qdap)
#Read the Hotel reviews dataset
reviews <- read.csv("Hotel_Reviews.csv")
#Check the polarity score for the reviews
#Polarity score for negative reviews
neg_polarity <- polarity(reviews$Negative_Review)

