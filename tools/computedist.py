"""
Computes path distance
"""
import math
import csv
def extractpath(file,type):
	"""Read path from tsp and csv files"""
	with open(file,"rb") as f:
		if type=="tsp":
			path=[int (i) for i in f.read().splitlines()[6:-2]]
		if type=="csv":
			path1=[i for i in f.read().splitlines()[1:]]
			path=[int(i.split(",")[0])+1 for i in path1]
			
	return path
def euc(c1,c2):
	"""Computes euclidean distance"""
	x1,y1=c1[0],c1[1]
	x2,y2=c2[0],c2[1]
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def dist(path):
	"""Computes distance of path"""
	coords={}
	with open("../raw/santa_cities.csv","rb") as f:
		for i in csv.reader(f):
			coords[int(i[0])+1]=[int(j) for j in i[1:]]
	dist=0
	print "Number of cities: ",len(path)
	for i in range(len(path)-1):
		dist+=euc(coords[path[i]],coords[path[i+1]])
	return dist

def validate(path):
	print len(path)
	for i in range(1,150001):
		if not i in path:
			print i,"not in path"
	
	assert len(path)==150000




if __name__ == "__main__":
	path=extractpath("../LKH/results/fans.csv","csv")
	print len(path)
	print dist(path)
	validate(path)
	path2=extractpath("../LKH/results/fans2p.csv","csv")
	print len(path2)
	print dist(path2)
	validate(path2)