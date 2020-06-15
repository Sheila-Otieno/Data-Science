import sklearn
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
from sklearn import cluster


wine_quality=pd.read_csv("winequality-white.csv",delimiter=";")
#print(wine_quality,"white wine")
categories = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide',
              'density', 'pH', 'sulphates', 'alcohol', 'quality']


wq = pd.DataFrame(wine_quality)
#print(wq)
fixed_acidity = wq.groupby(['fixed acidity'])
#for i in fixed_acidity:
#print(i)
#clf = svm.SVC(gamma=0.001, C=100.)
#print(clf.fit(wine_quality[:-1],wine_quality[:0]))
n_cluster = 3
k_means = cluster.KMeans(n_cluster)
print(k_means.fit(fixed_acidity))
print(k_means.labels_[::12])
#plt.plot(k_means)
#plt.show()

svc = svm.SVC(C=1, kernel='linear')
#print(svc.fit(wine_quality[:-100],categories[:-100]).score(wine_quality[-100:],categories[-100:]))


