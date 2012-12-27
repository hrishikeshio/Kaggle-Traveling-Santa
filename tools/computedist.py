def calc(file):
	with open(file,"rb") as f:
		path=[int (i) for i in f.read().splitlines()[6:-2]]
	return path
if __name__ == "__main__":
	path=calc("besttour_tot.tsp")
	print len(path)
	print path[:5]