#!/usr/bin/env python

# From view-source:http://www.pythonchallenge.com/pc/def/equality.html
# Read in arbitrary text, print any lower case letter with exactly three
# upper case letters both before and after it.

my_file = open("input.txt", "r")
garbage = my_file.read()
my_file.close()

message = ""
before = 0
after = 0
run = 0
possible = ""

for letter in garbage:
	#print "==="
	#print letter
	#print run
	#print before
	#print after
	#print possible
	#print "==="

	if letter.isupper():
		run = run + 1
	else:
		if run == 3:
			if before == 0:
				before = 1
				run = 0
				if possible == "":
					possible = letter
			elif after == 0:
				if possible in "abcdefghijklmnopqrstuvwxyz":
					message = message + possible
				run = 0
				before = 0
				after = 0
				possible = ""
		else:
			possible = ""
			run = 0
			before = 0
			after = 0

print message
