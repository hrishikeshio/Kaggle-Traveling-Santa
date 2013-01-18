"""
Runs LKH one by one
"""
import subprocess
import os
gridsize=8
os.chdir("../LKH")
for i in range(gridsize):
	for j in range(gridsize):
		print i,j
		ass=subprocess.Popen(["./LKH","cut"+str(i)+"_"+str(j)+".par"])
		ass.wait()