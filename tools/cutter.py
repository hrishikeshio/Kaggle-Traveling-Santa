import numpy as np 
import csv
coords=[]
with open("../raw/santa_cities.csv", "rb") as f:
    for i in csv.reader(f):
        coords.append([int(j) for j in i] )

coords=np.array(coords)
for i in range(10):
	with open("temp/cut"+str(i),"wb") as f:
		csv.writer(f).writerow(coords[np.where(coords<2000)])

	break