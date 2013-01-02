"""
Scipy distance matrix function
Defunct because of out of memory on huge matrix
"""
from scipy.spatial.distance import pdist,squareform
import csv
import math
import time
import numpy as np 
from computedist import extractpath
for c in range(6):
	for d in range(6):
		problem=str(c)+str(d)
		
		#Read coords
		coords=[]
		with open("../LKH/cut"+problem+".csv", "rb") as f:
		    for i in csv.reader(f):
		        coords.append([int(j) for j in i[1:]])
		print len(coords)
		
		#Create distance matrix
		ans=(pdist(coords,"euclidean"))

		sans2=[int(b) for b in ans]
		mapper={}
		
		#Read mapper
		with open("../LKH/mapper"+problem+".csv", "rb") as f:
			for i in csv.reader(f):
				mapper[int(i[1])]=int(i[0])
		
		#fans1l1=extractpath("../tools/temp/fans.csv","csv")
		fans1l1=extractpath("../LKH/besttour_totcut"+problem+".tsp","tsp")
		fans1l2=[-1]+(fans1l1)
		fans1=zip(fans1l1,fans1l2)
		#print fans1[1:5]
		print problem
		#exit()
		for i in fans1[1:]:
			lower,higher= (i[0],i[1]) if  (i[0]<i[1]) else (i[1],i[0])
			idx=(lower*higher-lower*(lower+1)/2)-1			
			sans2[idx]=10000
		"""
		011111
		001111
		000111
		000011
		000001
		n=(i*j-i(i+1)/2)-1
		=3*6-3*4/2
		=12
		"""
		start=0
		fans=[]
		for i in range(len(coords),0,-1):
			fans.append(sans2[start:start+i-1])
			start+=i-1
		sans2=[]
		
		#Write distance matrix
		with open("../LKH/dm"+problem+".tsp","wb") as ff:
			ff.write("NAME : cutter\n"+\
					"TYPE : TSP\n"+\
					"DIMENSION : "+str(len(coords))+"\n"+\
					"EDGE_WEIGHT_TYPE : EXPLICIT\n"+\
					"EDGE_WEIGHT_FORMAT : UPPER_ROW\n"+\
					"NODE_COORD_TYPE : NO_COORDS\n"+\
					"EDGE_WEIGHT_SECTION\n")
		
			csv.writer(ff,delimiter=" ").writerows(fans)