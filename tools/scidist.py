from scipy.spatial.distance import pdist
import csv
import math
import time
import numpy as np 
coords=[]
with open("../raw/santa_cities.csv", "rb") as f:
    for i in csv.reader(f):
        coords.append([int(j) for j in i] )
#coords=np.array(coords)
print coords[0]
init=[0,4360,6178]
cnt=0
a=time.time()

ans=pdist(coords,"cityblock")
with open("temp\grid2","wb") as f:
	for i in range(150000):
		cnt=0
		csv.writer(f).writerow(res[cnt:i])
		cnt=cnt+i