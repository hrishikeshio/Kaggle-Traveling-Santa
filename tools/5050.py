fans=[]
from computedist import dist, validate
"""
Add all solutions in array fans
"""
import csv
cnt=0
for i in range(6):
	for j in range(6):
		problem=str(i)+str(j)
		#path=2
		path=1 if j<2 else 2
		#path=1 if cnt%2==0 else 2
		cnt+=1
		with open("../LKH/path"+str(path)+"/ans"+problem+".csv","rb") as f:
			add=[k for k in csv.reader(f)]
			#add.reverse()
			fans+=add
print len(fans)
fans2=[]

"""
Add all solutions in array fans
"""
cnt=0
for i in range(6):
	for j in range(6):
		problem=str(j)+str(i)
		path=1
		path=2 if i<2 else 1
		#path=2 if (cnt)%2==0 else 1
		cnt+=1
		with open("../LKH/path"+str(path)+"/ans"+problem+".csv","rb") as f:
			add=[k for k in csv.reader(f)]
			add.reverse()
			fans2+=add

'''	for j in range(3,6):
		problem=str(i)+str(j)
		with open("../LKH/path2/ans"+problem+".csv","rb") as f:
			add=[k for k in csv.reader(f)]
			add.reverse()
			fans2+=add'''
print len(fans2)
fans1i=[int(i[0]) for i in fans]
fans2i=[int(i[0]) for i in fans2]
fans1ip1=[int(i[0])+1 for i in fans]
fans2ip1=[int(i[0])+1 for i in fans2]

#for i in fans1i:
#	print i

print dist(fans1ip1)
print dist(fans2ip1)
#print validate(fans1i)
#print validate(fans2i)
#print fans1i[:5]
fans1iw=[[i] for i in fans1i]
fans2iw=[[i] for i in fans2i]
with open("../LKH/results/mingle20/mingle1.csv","wb") as f:
	csv.writer(f).writerow(["path1"])
	csv.writer(f).writerows(fans1iw)

with open("../LKH/results/mingle20/mingle2.csv","wb") as f:
	csv.writer(f).writerow(["path2"])
	csv.writer(f).writerows(fans2iw)
