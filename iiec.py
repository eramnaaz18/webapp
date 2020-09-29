#!/usr/bin/python3
import cgi
import subprocess
print("content-type: text/html")
print()

form=cgi.FieldStorage()
order=form.getvalue("ord")
name=form.getvalue("name")
value=form.getvalue("val")
order=order.lower();
cmd=""
if not("don't" in order or "do not" in order):
	if "date" in order:
		print("Date is : ")
		cmd="date"
		print(subprocess.getoutput(cmd))
	elif "cal" in order:
		print("The calender for the present month is: ")
		cmd="cal"
		print(subprocess.getoutput(cmd))
	elif "ip" in order or "network" in order or "address" in order:
		print("Network details are: ")
		if name!=None:
			cmd="ifconfig {}".format(name)
		else:
			cmd="ifconfig"
		print(subprocess.getoutput(cmd))
	elif "list" in order or "show" in order or "ls" in order:
		if name!=None:
			if value==None:
				cmd="sudo ls {}".format(name)
			elif value=="long":
				cmd="sudo ls -l {}".format(name)
		else:
			if value==None:
				cmd="sudo ls"
			elif value=="long":
				cmd="sudo ls -l"
		print(subprocess.getoutput(cmd))
	elif "present" in order or "directory" in order:
		print("Present working directory is: ")
		cmd="pwd"
		print(subprocess.getoutput(cmd))
	elif "storage" in order or "volume" in order:
		print("Storage details are: ")
		cmd="sudo df -h"
		print(subprocess.getout(cmd))
	else:
		print("Invalid entry")

		cmd="sudo "+value
		print(subprocess.getoutput(cmd))
