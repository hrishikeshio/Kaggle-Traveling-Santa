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
	return list(p1s.intersection(p2s))

if __name__=="__main__":
	"""for i in range(6):
		for j in range(6):
			problem=str(i)+str(j)
			print problem
			#res=intersect("../LKH/besttour_totcut"+problem+".tsp","tsp","../LKH/path1/besttour_totcut"+problem+".tsp","tsp")
			print len(res)
			print res[:5]"""
	#res=intersect("../LKH/besttour_totcut03.tsp","tsp","../LKH/path1/besttour_totcut03.tsp","tsp")
	#res=intersect("../LKH/results/time300/fans.csv","csv","../LKH/results/time300/fans2.csv","csv")
	#res=intersect("../LKH/results/mingle/fans1.csv","csv","../LKH/results/mingle/fans2.csv","csv")
	res=intersect("../LKH/results/mingle/mingle1.csv","csv","../LKH/results/mingle/mingle2.csv","csv")
	print "fin",len(res)
	#print res