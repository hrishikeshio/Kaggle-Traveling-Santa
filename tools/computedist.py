import math
import csv
def extractpath(file,type):
	with open(file,"rb") as f:
		if type=="tsp":
			path=[int (i) for i in f.read().splitlines()[6:-2]]
		if type=="csv":
			path1=[i for i in f.read().splitlines()[1:]]
			path=[int(i.split(",")[0])+1 for i in path1]
			
	return path
def euc(c1,c2):
	#print c1,c2
	x1,y1=c1[0],c1[1]
	x2,y2=c2[0],c2[1]
	#print x1,x2,y1,y2
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def dist(path):
	coords={}
	with open("../raw/santa_cities.csv","rb") as f:
		for i in csv.reader(f):
			coords[int(i[0])+1]=[int(j) for j in i[1:]]
	dist=0
	print len(path)
	#print path[142722]
	#print coords[path[142721]]
	#print coords[path[142722]]
	#print euc(coords[path[142721]],coords[path[142722]])
	for i in range(len(path)-1):
	#for i in range(4):
		#print i
		dist+=euc(coords[path[i]],coords[path[i+1]])
		#print dist
	return dist


if __name__ == "__main__":
	path=extractpath("../results/besttour_tot.tsp","tsp")
	print len(path)
	print dist(path)
	path2=extractpath("../tools/temp/fans.csv","csv")
	#path=extractpath("../raw/random_paths_benchmark.csv","csv")
	print len(path2)
	#print path[142720:142725]
	print dist(path2)