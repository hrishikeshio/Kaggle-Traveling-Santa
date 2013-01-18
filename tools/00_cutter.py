"""
Cuts map into pieces of 3334x3334
"""

import numpy as np 
import csv
coords=[]
gridsize=8
squaresize=20000./gridsize
"""
Read raw data
"""
with open("../raw/santa_cities.csv", "rb") as f:
    for i in csv.reader(f):
        coords.append([int(j) for j in i] )

coords=np.array(coords)
"""
Cut it
"""

for i in range(gridsize):
	for j in range(gridsize):

		with open("../LKH/temp/cut"+str(i)+"_"+str(j)+".csv","wb") as f:
			logx=np.logical_and(coords[:,1]>=i*squaresize,coords[:,1]<(i+1)*squaresize)
			logy=np.logical_and(coords[:,2]>=j*squaresize,coords[:,2]<(j+1)*squaresize)
			logass=np.logical_and(logx,logy)
			#create mapper files which map between original names and new names
			fmapper=open("../LKH/temp/mapper"+str(i)+"_"+str(j)+".csv","wb")
			csv.writer(fmapper).writerows(zip([k+1 for k in range(len(coords[logass]))],coords[logass,0]))
			fmapper.close()
			csv.writer(f).writerows(coords[logass])
			#Create .par files for LKH			
			g=open("../LKH/cut"+str(i)+"_"+str(j)+".par","wb")
			g.write("""PROBLEM_FILE =dm"""+str(i)+"_"+str(j)+".tsp"+"""
#CANDIDATE_FILE = candidates_totcut"""+str(i)+str(j)+".tsp"+"""
INITIAL_TOUR_ALGORITHM = NEAREST-NEIGHBOR
RUNS = 1
SEED = 1
MAX_CANDIDATES = 6
TIME_LIMIT = 1
TOUR_FILE = besttour_totcut"""+str(i)+"_"+str(j)+".tsp"+"""
""")
			g.close()

		