import csv
inn=[]
with open("../LKH/besttour_totcut00.tsp","rb") as f:
	inputf=csv.reader(f)
	for i in inputf:
		inn.append(i)
print inn[-5:]
inn=[int(i[0]) for i in inn[6:-2]]
print inn[:5]