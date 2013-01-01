"""
Scipy distance matrix function
Defunct because of out of memory on huge matrix
"""
from scipy.spatial.distance import pdist,squareform
import csv
import math
import time
import numpy as np 

	#with open("../raw/santa_cities.csv", "rb") as f:
for c in range(6):
	for d in range(6):
		coords=[]
		problem=str(c)+str(d)
		with open("temp/cut"+problem+".csv", "rb") as f:
		#with open("pr2392.tsp", "rb") as f:

		    for i in csv.reader(f):
		        coords.append([int(j) for j in i[1:]] )
		#coords=np.array(coords)
		print len(coords)
		#print coords[:5]

		a=time.time()
		ans=(pdist(coords,"euclidean"))
		#print len(ans)
		with open("../LKH/"+problem+"dm.tsp","wb") as f:
			f.write("""NAME : cutter
TYPE : TSP
DIMENSION : """+str(len(coords))+"""
EDGE_WEIGHT_TYPE : EXPLICIT
EDGE_WEIGHT_FORMAT : UPPER_ROW
NODE_COORD_TYPE : NO_COORDS
EDGE_WEIGHT_SECTION
""")
			#sans=squareform(ans)

			sans2=[]

			sans2=[int(b) for b in ans]
			ans=[]
		#	csv.writer(f,delimiter=" ").writerows(sans2)
			print problem
			start=0
			fans=[]
			for i in range(len(coords),0,-1):
				#print i

				#print start,start+i-1
				fans.append(sans2[start:start+i-1])
				start+=i-1
				#start=start+current
				#current =start+ 6972-i-1
			#print [len(i) for i in fans]
			#print fans[:5]
			#print len(fans)
			sans2=[]
			csv.writer(f,delimiter=" ").writerows(fans)
		"""0:2393
		2393:(2393*2)-1
		(2393*2)-1:"""