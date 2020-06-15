import sklearn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import linear_model


wine_quality=pd.read_csv("winequality-white.csv",delimiter=";")
#print(wine_quality.head())
#print(wine_quality['pH'])
#print(wine_quality['quality'])
print(wine_quality.shape)
categories = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
              'density', 'pH', 'sulphates', 'alcohol']
#categories=['fa','va','ca','rs','ch','fsd','tsd','dn','ph','su','al']
#categories = [wine_quality['fixed acidity'], wine_quality['volatile acidity'],wine_quality['citric acid'],
#wine_quality['residual sugar'],wine_quality['chlorides'],wine_quality['free sulfur dioxide'],
#wine_quality['total sulfur dioxide'],wine_quality['density'],wine_quality['pH'],
#wine_quality['sulphates'],wine_quality['alcohol']]
fa = wine_quality['fixed acidity']
va = wine_quality['volatile acidity']
ca = wine_quality['citric acid']
rs = wine_quality['residual sugar']
ch = wine_quality['chlorides']
fsd = wine_quality['free sulfur dioxide']
tsd = wine_quality['total sulfur dioxide']
dn = wine_quality['density']
ph = wine_quality['pH']
su = wine_quality['sulphates']
al = wine_quality['alcohol']

X=wine_quality[categories]
y=wine_quality['quality']
#linear regression
lm = linear_model.LinearRegression()
model = lm.fit(X, y)
predictions = lm.predict(X)
print(predictions,"predictions")
print(lm.score(X, y),"score")

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

print('Accuracy of Logistic regression classifier on training set: {:.2f}'
      .format(logreg.score(X_train, y_train)))
print('Accuracy of Logistic regression classifier on test set: {:.2f}'
      .format(logreg.score(X_test, y_test)))

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print('Accuracy of K-NN classifier on training set: {:.2f}'
      .format(knn.score(X_train, y_train)))
print('Accuracy of K-NN classifier on test set: {:.2f}'
      .format(knn.score(X_test, y_test)))

clf = DecisionTreeClassifier().fit(X_train, y_train)

print('Accuracy of Decision Tree classifier on training set: {:.2f}'
      .format(clf.score(X_train, y_train)))
print('Accuracy of Decision Tree classifier on test set: {:.2f}'
      .format(clf.score(X_test, y_test)))
clf2 = DecisionTreeClassifier(max_depth=3).fit(X_train, y_train)
print('Accuracy of Decision Tree classifier on training set: {:.2f}'
      .format(clf2.score(X_train, y_train)))
print('Accuracy of Decision Tree classifier on test set: {:.2f}'
      .format(clf2.score(X_test, y_test)))
svm = SVC()
svm.fit(X_train, y_train)

print('Accuracy of SVM classifier on training set: {:.2f}'
      .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
      .format(svm.score(X_test, y_test)))
pred = knn.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

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




