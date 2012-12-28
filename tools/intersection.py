from computedist import extractpath
def intersect(file1,type1,file2,type2):
	p1l=extractpath(file1,type1)
	p1l2=[-1]+(p1l)
	p1=zip(p1l,p1l2)
	p1s=set([frozenset(i)for i in p1])

	p2l=extractpath(file2,type2)
	p2l2=[-1]+(p2l)
	p2=zip(p2l,p2l2)
	p2s=set([frozenset(i)for i in p2])
	return p1s.intersection(p2s)

if __name__=="__main__":
	res=intersect("../results/besttour_tot.tsp","tsp","../results/hilbert_santa_path.csv","csv")
	print len(res)
	#print res