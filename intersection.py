from computedist import calc
def intersect(file1,type1,file2,type2):
	p1l=calc(file1,type1)
	p1l2=[-1]+(p1l)
	p1=zip(p1l,p1l2)
	p1s=set([frozenset(i)for i in p1])

	p2l=calc(file2,type2)
	p2l2=[-1]+(p2l)
	p2=zip(p2l,p2l2)
	p2s=set([frozenset(i)for i in p2])
	return p1s.intersection(p2s)

if __name__=="__main__":
	res=intersect("besttour_tot.tsp","tsp","raw/random_paths_benchmark.csv","csv")
	print len(res)
	print res