import os
import shutil
from os import listdir
from os.path import isfile, join

total_acc = 0
cluster_size = 25
F = open("RESLUT.txt","w")
F.write("TRAINING RESULT \n")
result_train_path = "./data/result_train/"
onlyfiles = [f for f in listdir(result_train_path) if isfile(join(result_train_path, f))]
total_data = 0
for i in range(len(onlyfiles)):
    filename = result_train_path + onlyfiles[i]
    print(onlyfiles[i])
    file = open(filename, "r")
    data = []
    for i in range(101):
        data.append(0)
    for line in file:
        line =  line.splitlines()
        cluster = int(float(line[0]))
        data[cluster] = data[cluster] + 1
    data_sort = sorted(data)
    total_data = sum(data) + total_data
    #print(total_data)
    #print(data)
    print(data_sort)
    acc = (data_sort[len(data_sort) - 1])
    #acc = (data_sort[len(data_sort) - 1] + data_sort[len(data_sort) - 2] + data_sort[len(data_sort) - 3])
    #acc = (data_sort[len(data_sort) - 1]+data_sort[len(data_sort) - 2]+data_sort[len(data_sort) - 3]+data_sort[len(data_sort) - 4]+data_sort[len(data_sort) - 5])
    #print(acc)
    total_acc = total_acc + acc
    #F.write(str(acc)+"\n")
    max = [-10,-10,-10,-10,-10]
    max_index = [-1,-1,-1,-1,-1]
    for j in range(len(data)):
        for k in range(5):
            if data[j] > max[k]:
                max[k] = data[j]
                max_index[k] = j
                break
    print("CLUSTER GOT ", max_index)

print("TOTAL ACC ", total_acc/total_data)
F.write("TOTAL ACC " +  str(total_acc/total_data) + "\n")
F.write("TESTING RESULT \n")
print("TESTING")

total_acc = 0
total_data = 0
result_train_path = "/Users/Omar/Desktop/580/Project/data/result_test/"
onlyfiles = [f for f in listdir(result_train_path) if isfile(join(result_train_path, f))]
for i in range(len(onlyfiles)):
    filename = result_train_path + onlyfiles[i]
    file = open(filename, "r")
    data = []
    for i in range(101):
        data.append(0)
    for line in file:
        line = line.splitlines()
        cluster = int(float(line[0]))
        data[cluster] = data[cluster] + 1
    data_sort = sorted(data)
    total_data = sum(data) + total_data
    #print(total_data)
    #print(data)
    print(data_sort)
    #acc = (data_sort[len(data_sort) - 1] + data_sort[len(data_sort) - 2] + data_sort[len(data_sort) - 3])
    #acc = (data_sort[len(data_sort) - 1] + data_sort[len(data_sort) - 2] + data_sort[len(data_sort) - 3] + data_sort[
     #  len(data_sort) - 4] + data_sort[len(data_sort) - 5])
    acc = (data_sort[len(data_sort) - 1])
    print(acc)
    total_acc =total_acc + acc
    F.write(str(acc) + "\n")
    max = -10
    max_index = -1
    max = [-10, -10, -10, -10, -10]
    max_index = [-1, -1, -1, -1, -1]
    for j in range(len(data)):
        for k in range(5):
            if data[j] > max[k]:
                max[k] = data[j]
                max_index[k] = j
                break
    print("CLUSTER GOT ", max_index)
print("TOTAL ACC ", total_acc/total_data)
F.write("TOTAL ACC " +  str(total_acc/total_data) + "\n")

F.close()