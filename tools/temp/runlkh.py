import csv
import subprocess
import sys

for i in range(4):
	for j in range(4):
		print i,j
		call=subprocess.Popen(["./LKH", "cut"+str(i)+str(j)+".par"])
		call.wait()