"""
Cuts map into pieces of 5000x5000
"""

import numpy as np 
import csv
coords=[]
with open("../raw/santa_cities.csv", "rb") as f:
    for i in csv.reader(f):
        coords.append([int(j) for j in i] )

coords=np.array(coords)
for i in range(6):
	for j in range(6):

		with open("temp/cut"+str(i)+str(j)+".csv","wb") as f:
			logx=np.logical_and(coords[:,1]>=i*3334,coords[:,1]<(i+1)*3334)
			logy=np.logical_and(coords[:,2]>=j*3334,coords[:,2]<(j+1)*3334)
			logass=np.logical_and(logx,logy)
			coords[logass,0]=[k+1 for k in range(len(coords[logass]))]
			csv.writer(f).writerows(coords[logass])
			h=open("temp/cut"+str(i)+str(j)+".tsp","wb")
			h.write("""NAME : pr2392
COMMENT : file cut by cutter.py
TYPE : TSP
DIMENSION :"""+str(len(coords[logass]))+"""
EDGE_WEIGHT_TYPE : EUC_2D
NODE_COORD_SECTION
""")
			csv.writer(h,delimiter=' ').writerows(coords[logass])
			h.close()
			g=open("../LKH/cut"+str(i)+str(j)+".par","wb")
			g.write("""PROBLEM_FILE = cut"""+str(i)+str(j)+".tsp"+"""
CANDIDATE_FILE = candidates_totcut"""+str(i)+str(j)+".tsp"+"""
INITIAL_TOUR_ALGORITHM = NEAREST-NEIGHBOR
RUNS = 1
SEED = 1
MAX_CANDIDATES = 6
TIME_LIMIT = 40
TOUR_FILE = besttour_totcut"""+str(i)+str(j)+".tsp"+"""
""")
			g.close()

		