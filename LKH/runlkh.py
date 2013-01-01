import csv
import subprocess
import sys

for i in range(6):
	for j in range(6):
		print i,j
		call=subprocess.Popen(["./LKH", "cut"+str(i)+str(j)+".par"])
		call.wait()
