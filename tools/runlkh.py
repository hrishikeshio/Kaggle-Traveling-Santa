"""
Runs LKH one by one
"""
import csv
import subprocess
import sys

for i in range(6):
	for j in range(6):
		print i,j
        ass=subprocess.call(["./LKH", "dm"+str(i)+str(j)+".par"])
        ass.wait()