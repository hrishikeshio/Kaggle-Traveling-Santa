"""
Computes common edges from 2 paths
"""
from computedist import extractpath

def intersect(file1,type1,file2,type2):
	p1l1=extractpath(file1,type1)
	p1l2=[-1]+(p1l1)
	p1=zip(p1l1,p1l2)
	p1s=set([frozenset(i)for i in p1])

	p2l1=extractpath(file2,type2)
	p2l2=[-1]+(p2l1)
	p2=zip(p2l1,p2l2)
	p2s=set([frozenset(i)for i in p2])
	return p1s.intersection(p2s)

if __name__=="__main__":
	res=intersect("../results/besttour_tot.tsp","tsp","../tools/temp/fans.csv","csv")
	print len(res)
	#print res