"""
Scipy distance matrix function
"""
from scipy.spatial.distance import pdist,squareform
import csv
import math
import time
import numpy as np 
from computedist import extractpath
secondpath=True
aset="1"
adjust=False
gridsize=8

adjust= "ad" if adjust==True else ""
def createdm(sans2,width):
	start=0
	fans=[]
	#print len(coords)
	for i in range(width,1,-1):
		fans.append(sans2[start:start+i-1])
		start+=i-1
	sans2=[]
	return fans			
def makeinf(fans,ans,width):
	for i in fans[1:]:
		a,b= (i[0],i[1]) if  (i[0]<i[1]) else (i[1],i[0])
		#idx=(a-1)*(b-1)+(a+1)*(a+2)/2-1
		idx=width*(a)-a*(a+1)/2-(width-b)-1
         
		#idx=(lower*higher-lower*(lower+1)/2)-1	
		
		try:		
			ans[idx]=1000000
		except:
			print"exception", lower,higher,idx,len(ans)
	return ans

	
def run():			
	for c in range(gridsize):
		for d in range(gridsize):
			problem=str(c)+"_"+str(d)
			
			#Read coords
			coords=[]
			with open("../LKH/temp/"+adjust+"cut"+problem+".csv", "rb") as f:
			    for i in csv.reader(f):
			        coords.append([int(j) for j in i[1:]])
			print len(coords)
			ans=[]
			#Create distance matrix
			ans=(pdist(coords,"euclidean"))
			sans2=[]
			sans2=[int(b) for b in ans]
			mapper={}
			
			#Read mapper
			with open("../LKH/temp/"+adjust+"mapper"+problem+".csv", "rb") as f:
				for i in csv.reader(f):
					mapper[int(i[1])]=int(i[0])
			
			print problem
			width=len(coords)
			
			if secondpath:
				fans1l1=extractpath("../LKH/s"+aset+"path1/besttour_totcut"+problem+".tsp","tsp")
				fans1l2=[-1]+(fans1l1)

				fans1=zip(fans1l1,fans1l2)
				#print fans1[1:5]
				sans2=makeinf(fans1,sans2,width)
	
			fans=[]
			fans=createdm(sans2,width)
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
	
if __name__=="__main__":
	run()