#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        
        for x in range(len(word)):
        	try:
        		print (("%s%s\t\t%s") % (word[x],word[x+1], 1))
        	except:
        		pass
