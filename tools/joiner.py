"""
Joins solutions
"""
import csv

fans=[]

"""
read cut files and solutions and rewrite them as real city numners
"""
for i in range(4):
	for j in range(4):
		problem=str(i)+str(j)
		orig=[]
		with open("temp/cut"+problem+".csv","rb") as f:

			for k in csv.reader(f,delimiter=" "):
				orig.append([int(k[0])]+k[1:])
		ans=[]
		with open("temp/besttour_totcut"+problem+".tsp","rb") as f:
			lines=f.readlines()
			ans=lines[6:-2]
			#print lines[-5:-2]
			ans=[int(word.strip())-1 for word in ans]
		with open("temp/ans"+problem+".csv","wb") as f:
			csv.writer(f).writerows([[orig[m][0]] for m in ans])

fans=[]

"""
Add all solutions in array fans
"""

for i in range(4):
	for j in range(4):
		problem=str(i)+str(j)
		with open("temp/ans"+problem+".csv","rb") as f:
			fans=fans+[k for k in csv.reader(f)]
fanset=set([])

"""
Make sure all cities exist
"""
for i in fans:
	fanset.add(int(i[0]))
for i in range(150000):
	if not i in fanset:
		print i
		
"""
write final solutions
"""
with open("temp/fans.csv","wb") as f:
	csv.writer(f).writerow(["path"])
	csv.writer(f).writerows(fans)
