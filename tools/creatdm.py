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
#with open("temp\grid","wb") as f:
#	pass

res=np.zeros(150000-cnt,dtype=np.int)
with open("temp\grid","wb") as f:
	for init in coords:
		cnt+=1
		print cnt
		#res=[]
		#for i in coords[cnt:]:
		#	res.append(abs(init[1]-i[1])+abs(init[2]-i[2]))
		for i in range(len(coords[cnt:])):
			res[i]=abs(init[1]-coords[i][1])+abs(init[2]-coords[i][2])
		
		csv.writer(f).writerow(res[cnt:])
		#with open("temp\grid"+str(cnt),"wb") as f:
		#	csv.writer(f).writerows([res])
		#print len(res)
		print time.time()-a
