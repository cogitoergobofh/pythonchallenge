#!/usr/bin/env python

# http://www.pythonchallenge.com/pc/def/linkedlist.php
# Iterate through list of nothings.  Prompt for a starting nothing, and
# iterate through them until failure.  On failure, print page text.

import urllib
import re

baseurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = input('Enter starting nothing: ')
nothing = str(nothing)
print 'Starting nothing is: ' + nothing + '.'

for request in range(400):
	url = baseurl + nothing
	print "Retrieving: " + url
	nothingpage = urllib.urlopen(url)
	nothingstring = str(nothingpage.read())
	nothingpage.close()

	try:

	        nothingarray = re.split('nothing is', nothingstring, flags=re.IGNORECASE)
	        nothing = nothingarray[1].strip()
	except:
		print('Failed to match nothing.  Page text is:')
		print nothingstring
		break
