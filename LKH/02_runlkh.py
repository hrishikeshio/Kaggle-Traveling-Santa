"""
Runs LKH one by one
"""
import subprocess

for i in range(6):
	for j in range(6):
		print i,j
		ass=subprocess.Popen(["./LKH","cut"+str(i)+str(j)+".par"])
		ass.wait()