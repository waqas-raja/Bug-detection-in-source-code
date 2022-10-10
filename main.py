import pandas as pd
import numpy as np
import os
import csv

path = "DataSet/bufferOverflow"
# testPath = "DataSet/testData"
count = 0
errorType = "buffer overflow"
arr = []

for path, subdirs, files in os.walk(path):
    for name in files:
        if(".c" in name and "-ok" not in name):
            groundTruth = 1
            filePath = os.path.join(path, name)
            f = open(filePath, "r")
            d = f.read()
            arr.append([d, groundTruth, errorType])
            count += 1
        elif("-ok" in name):
            groundTruth = 0
            filePath = os.path.join(path, name)
            f = open(filePath, "r")
            d = f.read()
            arr.append([d, groundTruth, errorType])
            count += 1

# print(pd.DataFrame(arr))
# print(count)
pd.DataFrame(arr).to_csv('dataset_buffer_overflow.csv', index_label = "Id", header  = ['Code Desc', "Is Error", "Error Type"])