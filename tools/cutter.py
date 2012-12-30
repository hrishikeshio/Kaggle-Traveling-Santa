import numpy as np 
import csv
coords=[]
with open("../raw/santa_cities.csv", "rb") as f:
    for i in csv.reader(f):
        coords.append([int(j) for j in i] )

coords=np.array(coords)
for i in range(4):
	for j in range(4):
		with open("temp/cut"+str(i)+str(j)+".tsp","wb") as f:
			logx=np.logical_and(coords[:,1]>=i*5000,coords[:,1]<(i+1)*5000)
			logy=np.logical_and(coords[:,2]>=j*5000,coords[:,2]<(j+1)*5000)
			logass=np.logical_and(logx,logy)
			f.write("""NAME : pr2392
COMMENT : 2392-city problem (Padberg/Rinaldi)
TYPE : TSP
DIMENSION :"""+str(len(coords[logass]))+"""
EDGE_WEIGHT_TYPE : EUC_2D
NODE_COORD_SECTION
""")
			coords[logass,0]=[k+1 for k in range(len(coords[logass]))]
			csv.writer(f,delimiter=' ').writerows(coords[logass])
			g=open("temp/cut"+str(i)+str(j)+".par","wb")
			g.write("""PROBLEM_FILE = cut"""+str(i)+str(j)+".tsp"+"""
CANDIDATE_FILE = candidates_totcut"""+str(i)+str(j)+".tsp"+"""
INITIAL_TOUR_ALGORITHM = NEAREST-NEIGHBOR
RUNS = 1
SEED = 1
MAX_CANDIDATES = 6
TIME_LIMIT = 4000
TOUR_FILE = besttour_totcut"""+str(i)+str(j)+".tsp"+"""
""")
			g.close()

			#csv.writer(f).writerows(coords[np.where(20000*i<coords<2000*(i+1))[0]][:,1:])

		