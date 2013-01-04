"""
Scipy distance matrix function
"""
from scipy.spatial.distance import pdist,squareform
import csv
import math
import time
import numpy as np 
from computedist import extractpath

def makeinf(fans,ans):
	for i in fans[1:]:
		#print i
		i,j= (i[0],i[1]) if  (i[0]<i[1]) else (i[1],i[0])
		idx=(i-1)*(j-1)+(i+1)*(i+2)/2-1
		#idx=(lower*higher-lower*(lower+1)/2)-1	
		
		try:		
			ans[idx]=1000000
		except:
			print"exception", lower,higher,idx,len(ans)
		return ans

secondpath=False		
def run():			
	for c in range(6):
		for d in range(6):
			problem=str(c)+str(d)
			
			#Read coords
			coords=[]
			with open("../LKH/temp/cut"+problem+".csv", "rb") as f:
			    for i in csv.reader(f):
			        coords.append([int(j) for j in i[1:]])
			print len(coords)
			
			#Create distance matrix
			ans=(pdist(coords,"euclidean"))

			sans2=[int(b) for b in ans]
			mapper={}
			
			#Read mapper
			with open("../LKH/temp/mapper"+problem+".csv", "rb") as f:
				for i in csv.reader(f):
					mapper[int(i[1])]=int(i[0])
			
			#fans1l1=extractpath("../tools/temp/fans.csv","csv")
			print problem
			if secondpath:
				fans1l1=extractpath("../LKH/besttour_totcut"+problem+".tsp","tsp")
				fans1l2=[-1]+(fans1l1)

				fans1=zip(fans1l1,fans1l2)
				#print fans1[1:5]
				sans2=makeinf(fans1,sans2)
				
			"""  5
			011111
			001111
		   2000111
			000011
		   4000001
		   act14
		   5*6 -5*6/2-1=14
			n=(i*j-i*(i+1)/2)-1
			=2*5-2*3/2-1
			=10-3-1
			=6
			=3*6-3*4/2
			=12
			actual 11
			=(i+1)(j+1)-(i+1)*(i+2)/2 -1
			=3*6-3*4/2 -1
			=18-6-1
			=11

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
			with open("../LKH/temp/dm"+problem+".csv","wb") as ff:
				csv.writer(ff,delimiter=",").writerows(fans)

if __name__=="__main__":
	#fans=[(0,0),(3,2)]
	"""   23
	    01233
       100124
       200032
        00009
        n=(i*j-i*(i+1)/2)-1
        i,j=2,3
        n=(i-1)*(j-1)+(i+1)*(i+2)/2-1
         = 2+3*4/2-1
         =12
         act7
           """
	#sans=[1,2,3,3,1,2,4,3,2,9]
	#print sans
	#print makeinf(fans,sans)
	run()