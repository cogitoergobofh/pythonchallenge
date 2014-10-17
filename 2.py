#!/usr/bin/env python

# The OCR test: in a random string of garbage, print out the alphanumerics.
# input.txt from view-source:http://www.pythonchallenge.com/pc/def/ocr.html

my_file = open("input.txt", "r")
garbage = my_file.read()
my_file.close()

message = ""

for character in garbage:
	character = character.lower()
	if character in "abcdefghijklmnopqrstuvwxyz":
		message = message + character

print message

