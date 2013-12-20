import sys
import csv 

#select csv file

#open csv file
#cutting columns "csvcut -c"
filename = sys.argv[1]
x = sys.argv[2]
x = int(x) - 1
with open(filename, 'rb') as newfile: #examples found online didn't define 'rb' formatting option...i don't really see a difference
	readaline = csv.reader(newfile)
	for row in readaline:
		print row[x]

