"""
Joins solutions
"""
import csv

fans=[]
aset="1"
path="2"
gridsize=8
"""
read cut files and solutions and rewrite them as real city numners
"""
for i in range(gridsize):
	for j in range(gridsize):
		problem=str(i)+"_"+str(j)
		orig=[]
		with open("../LKH/temp/cut"+problem+".csv","rb") as f:

			for k in csv.reader(f):
				#print k

				orig.append([int(k[0])]+k[1:])

		ans=[]
		with open("../LKH/s"+aset+"path"+path+"/besttour_totcut"+problem+".tsp","rb") as f:
			lines=f.readlines()
			ans=lines[6:-2]
			#print lines[-5:-2]
			ans=[int(word.strip())-1 for word in ans]
			
		with open("../LKH/s"+aset+"path"+path+"/ans"+problem+".csv","wb") as f:
			csv.writer(f).writerows([[orig[m][0]] for m in ans])

fans=[]

"""
Add all solutions in array fans
"""

for i in range(gridsize):
	for j in range(gridsize):
		problem=str(j)+"_"+str(i)
		with open("../LKH/s"+aset+"path"+path+"/ans"+problem+".csv","rb") as f:
			add=[k for k in csv.reader(f)]
			add.reverse()
			fans+=add
fanset=set([])

"""
Make sure all cities exist
"""
for i in fans:
	fanset.add(int(i[0]))
for i in range(150000):
	if not i in fanset:
		print i," not in ans"
		
"""
write final solutions
"""
with open("../LKH/results/tiny8_1/fans2.csv","wb") as f:
	csv.writer(f).writerow(["path2"])
	csv.writer(f).writerows(fans)
