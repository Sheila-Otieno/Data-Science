import sklearn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import linear_model

#Load the csv file into a variable wine_quality
wine_quality=pd.read_csv("winequality-white.csv",delimiter=";")
#put all the input variables into an array of categories

categories = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
              'density', 'pH', 'sulphates', 'alcohol']

#create the X and y variable that will be used for machine learning
X=wine_quality[categories]
y=wine_quality['quality']

#linear regression
lm = linear_model.LinearRegression()
model = lm.fit(X, y)
predictions = lm.predict(X)
print("Predictions: ")
print(predictions)
print("Score: ")
print(lm.score(X, y))
print("Coefficients: ")
print(lm.coef_)
print("Intercept: ")
print(lm.intercept_)

#K-NN Classifier
#Create training and test sets and apply scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#perform the classification
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
      .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
      .format(knn.score(X_test, y_test)))

#confusion matrix
pred = knn.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

#plot the k in a graph
k_range = range(1, 20)
scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    scores.append(knn.score(X_test, y_test))
plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(k_range, scores)
plt.xticks([0, 5, 10, 15, 20])
plt.show()




