from computedist import calc
p1l=calc("besttour_tot.tsp")
p1l2=[-1]+(p1l)
print p1l[:5]
print p1l2[:5]
p1=zip(p1l,p1l2)
p1s=[]
for i in p1:
	p1s.append(set(i))
print p1s[:5]
print set([-1,1]) in p1s
