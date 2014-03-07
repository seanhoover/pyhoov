import re
import sys
csvfile = sys.argv[1]
row = int(sys.argv[2])

with open('~/pyhoov/' + csvfile) as file:
	for line in file:
		col = re.split(r'[, ]', line)
		print col[row]
