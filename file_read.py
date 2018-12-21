import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import os
import shutil


from os import listdir
from os.path import isfile, join
mypath = "/Users/Omar/Desktop/project_data/"

i = 0

for x in os.walk(mypath):
    if i == 0:
        i = i+1
        folder_name = x[1]

train_path = "./data/train/"
test_path = "./data/test/"

for i in folder_name:
    folder_path = mypath + i
    if os.path.exists(train_path + i) is False:
        os.makedirs(train_path + i)
    if os.path.exists(test_path + i) is False:
        os.makedirs(test_path + i)

    onlyfiles = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    train_len = int(len(onlyfiles)*.7)
    testlen = len(onlyfiles)-train_len

    for j in range(train_len):
        dir_src = folder_path
        dir_dst = train_path + i
        src_file = os.path.join(dir_src, onlyfiles[j])
        dst_file = os.path.join(dir_dst, onlyfiles[j])
        shutil.move(src_file, dst_file)
    for j in range(train_len, len(onlyfiles)):
        dir_src = folder_path
        dir_dst = test_path + i
        src_file = os.path.join(dir_src, onlyfiles[j])
        dst_file = os.path.join(dir_dst, onlyfiles[j])
        shutil.move(src_file, dst_file)

