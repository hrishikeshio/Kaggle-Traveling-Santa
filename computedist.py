def calc(file,type):
	with open(file,"rb") as f:
		if type=="tsp":
			path=[int (i) for i in f.read().splitlines()[6:-2]]
		if type=="csv":
			path1=[i for i in f.read().splitlines()[1:]]
			path=[int(i.split(",")[0]) for i in path1]
			
	return path
if __name__ == "__main__":
	path=calc("besttour_tot.tsp","tsp")
	path=calc("raw/random_paths_benchmark.csv","csv")
	print len(path)
	print path[:5]