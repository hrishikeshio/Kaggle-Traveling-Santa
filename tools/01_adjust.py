"""
in cuts, put leftmost point at top
and rightmost at bottom
etc
"""
import csv
import numpy as np
from computedist import euc
secondset=True
for i in range(6):
	for j in range(6):
		mind1=100000
		mind2=100000
		ans1=0
		ans2=0
		coords1=[i*3334,j*3334]
		#coords2=[(i+1)*3334,(j)*3334] if secondset else [(i)*3334,(j+1)*3334]
		problem=str(i)+str(j)
		#print coords2

		with open("../LKH/temp/cut"+problem+".csv","rb") as f:
			fr=[row for row in csv.reader(f)]
			for idx in range(len(fr)):
				row=fr[idx]
				if euc(coords1,row[1:])<mind1:
					mind1=euc(coords1,row[1:])
					ans1=row
					a1idx=idx
				'''if euc(coords2,row[1:])<mind2:
					mind2=euc(coords2,row[1:])
					ans2=row
					a2idx=idx'''
			print mind1#,mind2
			print ans1#,ans2
			print a1idx#,a2idx
			fr.remove(ans1) 
			#fr.remove(ans2)
			#fr.append(ans2)
			fr=[ans1]+fr
			fr=np.array(fr)
			#print fr[:,1:]
			exit()
			with open("../LKH/temp/adcut"+problem+".csv","wb") as g:
				gw=csv.writer(g)
				#gw.writerow(ans1)
				gw.writerows(fr)
			with open("../LKH/temp/admapper"+str(i)+str(j)+".csv","wb") as fmapper:
				csv.writer(fmapper).writerows(zip([k+1 for k in range(len(fr))],fr[:,0]))
			


