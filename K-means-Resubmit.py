import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

np.random.seed(12345)


# Function for loading the iris data
# load_data returns a 2D numpy array where each row is an example
#  and each column is a given feature.
def load_data():
    iris = datasets.load_iris()
    return iris.data


# Assign labels to each example given the center of each cluster
def assign_labels(X, centers):
    labels = []  
    for i in X:  
        center = i[0:2]  
        #calculate the distance of the nearest point to the center
        distance = []  
        for c in centers:  
            dist = np.sqrt(np.square(center[0] - c[0]) +np.square(center[1] - c[1]))
            distance.append(dist)

        label = [distance[0], 0]
        #assign labels based on distance of each point
        for j in range(len(distance)):  
            if(j == len(distance)-1):
                break
            elif(label[0] <= distance[j+1]):
                label = label
            else:
                label = [distance[j+1], j+1]

        labels.append(label[1])  

    return labels


# Calculate the center of each cluster given the label of each example
def calculate_centers(X, labels, K):
    centers = []
    #split the centers into two
    center1 = []
    center2 = []
    get_labels=np.unique(labels) #get the unique labels
    
    for k in range(K):    
        for i in range(len(get_labels)):
            initialX = X[i]  
            if(get_labels[i] == k):  
                center1.append(initialX[0:1])  
                center2.append(initialX[1:2])  
        centroids = [np.mean(center1), np.mean(center2)]#get the mean of the two centers
        
        centers.append(centroids)

    return centers


# Test if the algorithm has converged
# Should return a bool stating if the algorithm has converged or not.
def test_convergence(old_centers, new_centers):

    return np.array_equal(old_centers,new_centers)


# Evaluate the preformance of the current clusters
# This function should return the total mean squared error of the given clusters
def evaluate_performance(X, labels, centers):
    error_distance = 0  
    for i in range(len(X)):
        xCenters = labels[i]  
        current_center = centers[xCenters] 
        #get the cluster members
        c1 = X[i][0]  
        c2 = X[i][1]
        #calculate the distance between each point and the center 
        error_distance += np.sqrt(np.square(c1 - current_center[0]) + np.square(c2 - current_center[1]))
    
    #to get the sse we divide the distance of all points by the length of centers
    sse = error_distance/len(centers)  
    return sse


# Algorithm for performing K-means clustering on the give dataset
def k_means(X, K):
    if(K <= 0):  
        return np.Infinity, None  
    #find an initial k to start with by picking random values from the dataset
    initial_k = []
    for k in range(K):
        ink = X[np.random.randint(k, len(X))]
        initial_k.append(ink[0:2])
    #assign it to the old_centers
    old_centers = initial_k
    #stops when convergence is reached
    convergence = True
    while(convergence == True):
        #give labels to the old centers
        labels = assign_labels(X, old_centers)
        new_centers = calculate_centers(X, labels, K) #calculate new centers
        convergence = test_convergence(old_centers, new_centers)  # test to see if convergence has been reached

        old_centers = new_centers  # assign the new centers to the old and repeat the process again

    #evaluate the performance of the k-means
    sse = evaluate_performance(X, labels, new_centers)

    return (sse, labels,new_centers,X)


#plot the elbow method
def plotGraph(data):
    k_cluster = []
    for i in range(11):  
        se = k_means(data, i)
        k_cluster.append(se[0])

    print(k_cluster)

    return k_cluster


iris_data = load_data()
evaluation = plotGraph(iris_data)

plt.title("Elbow Method")  
plt.ylabel("SSE")
plt.xlabel("K")
plt.plot(evaluation)
plt.show()






