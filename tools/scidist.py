"""
Scipy distance matrix function
Defunct because of out of memory on huge matrix
"""
from scipy.spatial.distance import pdist,squareform
import csv
import math
import time
import numpy as np 
coords=[]
	#with open("../raw/santa_cities.csv", "rb") as f:
for c in range(10):
	with open("temp/cut"+str(c), "rb") as f:
	    for i in csv.reader(f):
	        coords.append([int(j) for j in i] )
	#coords=np.array(coords)
	print coords[0]
	init=[0,4360,6178]
	cnt=0
	a=time.time()

	ans=pdist(coords,"cityblock")
	with open("temp/sgrid"+str(c),"wb") as f:
		csv.writer(f).writerows(squareform(ans))