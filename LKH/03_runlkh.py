"""
Runs LKH one by one
"""
import csv
import subprocess
import sys
import os
run = os.system
for i in range(6):
	for j in range(6):
		print i,j
		ass=subprocess.Popen(["./LKH","cut"+str(i)+str(j)+".par"])
		ass.wait()