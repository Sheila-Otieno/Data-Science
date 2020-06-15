##LDA topic modelling
#read the Hotel reviews csv file
reviews <-read.csv("Hotel_Reviews.csv", header = TRUE)
str(reviews)
head(reviews, n=3)

#create a corpus of the text reviews
library(tm)
nreview_corpus <- VCorpus(VectorSource(reviews$Negative_Review))
print(nreview_corpus)
preview_corpus <- VCorpus(VectorSource(reviews$Positive_Review))
print(preview_corpus)

#clean the negative reviews data
nreview_corpus_clean <- tm_map(nreview_corpus,content_transformer(tolower))
nreview_corpus_clean <- tm_map(nreview_corpus_clean,stemDocument)
nreview_corpus_clean <- tm_map(nreview_corpus_clean, removeNumbers)
nreview_corpus_clean <- tm_map(nreview_corpus_clean, removeWords,stopwords())
nreview_corpus_clean <- tm_map(nreview_corpus_clean, removePunctuation)
nreview_corpus_clean <- tm_map(nreview_corpus_clean, stripWhitespace)

#clean the positive reviews data
preview_corpus_clean <- tm_map(preview_corpus,content_transformer(tolower))
preview_corpus_clean <- tm_map(preview_corpus_clean,stemDocument)
preview_corpus_clean <- tm_map(preview_corpus_clean, removeNumbers)
preview_corpus_clean <- tm_map(preview_corpus_clean, removeWords,stopwords())
preview_corpus_clean <- tm_map(preview_corpus_clean, removePunctuation)
preview_corpus_clean <- tm_map(preview_corpus_clean, stripWhitespace)

library(wordcloud)
wordcloud(nreview_corpus_clean, min.freq = 10, random.order = FALSE,
          colors=brewer.pal(8, "Dark2"))
