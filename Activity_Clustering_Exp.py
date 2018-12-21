import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import os
import shutil
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from os import listdir
from os.path import isfile, join
train_path = "/Users/Omar/Desktop/580/Project/data/train/"
test_path = "/Users/Omar/Desktop/580/Project/data/test/"
result_train_path = "/Users/Omar/Desktop/580/Project/data/result_train/"
result_test_path = "/Users/Omar/Desktop/580/Project/data/result_test/"
from sklearn.decomposition import PCA
i = 0

for x in os.walk(train_path):
    if i == 0:
        i = i+1
        folder_name = x[1]

cluster_size = 25

for i in range(cluster_size):
    folder_path = train_path + folder_name[i]
    onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    total_data = np.load(folder_path + "/" + onlyfiles[0])
    for j in range(1, len(onlyfiles)):
        data = np.load(folder_path + "/" + onlyfiles[j])
        total_data = np.concatenate((total_data, data), axis=0)






#mean = np.mean(total_data)
#total_data = total_data - mean

#pca = PCA(n_components=100)
#total_data = pca.fit_transform(total_data)

# Initializing KMeans
kmeans = KMeans(n_clusters=cluster_size)
# Fitting with inputs
kmeans = kmeans.fit(total_data)
# Predicting the clusters
#labels = kmeans.predict(total_data)



for i in range(cluster_size):
    folder_path = train_path + folder_name[i]
    onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    total_data = np.load(folder_path + "/" + onlyfiles[0])
    for j in range(1, len(onlyfiles)):
        data = np.load(folder_path + "/" + onlyfiles[j])
        total_data = np.concatenate((total_data, data), axis=0)
    #total_data = total_data - mean
    #total_data = pca.fit_transform(total_data)
    labels = kmeans.predict(total_data)
    np.savetxt(result_train_path + '/' + folder_name[i]+'.txt', labels)

for i in range(cluster_size):
    folder_path = test_path + folder_name[i]
    onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    total_data = np.load(folder_path + "/" + onlyfiles[0])
    for j in range(1, len(onlyfiles)):
        data = np.load(folder_path + "/" + onlyfiles[j])
        total_data = np.concatenate((total_data, data), axis=0)
    #total_data = total_data - mean
    #total_data = pca.fit_transform(total_data)
    labels = kmeans.predict(total_data)
    np.savetxt(result_test_path + '/' + folder_name[i]+'.txt', labels)