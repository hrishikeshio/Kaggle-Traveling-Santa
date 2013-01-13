import csv

with open("../LKH/results/mingle/mingle1.csv","rb") as f:
	with open("../LKH/results/mingle/mingle2.csv","rb") as g:
		with open("../LKH/results/mingle/minglesubm8.csv","wb") as h:
			fr=csv.reader(f)
			gr=csv.reader(g)
			p1=[]
			p2=[]
			p=[]

			for i in fr:
				p1.append(i[0])
			print p1[:5]
			for i in gr:
				p2.append(i[0])
			#p.append(["path1","path2"])
			for i in range(len(p1)):
				p.append([p1[i],p2[i]])
			csv.writer(h).writerows(p)
			print p[:5]