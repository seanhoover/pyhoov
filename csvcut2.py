
import csv 

#select csv file

csvfile = raw_input('Enter filename with path:')

#open csv file
#cutting columns "csvcut -c"
with open(csvfile, 'rb') as newfile: #examples found online didn't define 'rb' formatting option...i don't really see a difference
	readaline = csv.reader(newfile)
	for row in readaline:
		print row[0]

#parse the file

#close the file
