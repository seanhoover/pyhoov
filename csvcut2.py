#calling csvcut2 >> python <script_name> <column number>

import sys
import csv 

#cutting columns "csvcut -c"
filename = sys.argv[1]
column = sys.argv[2]
column = int(column) - 1
with open(filename, 'rb') as newfile: #examples found online didn't define 'rb' formatting option...i don't really see a difference
	readaline = csv.reader(newfile)
	for row in readaline:
		print row[column]

