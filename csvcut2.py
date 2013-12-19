
import csv 

#select csv file

csvfile = raw_input('Enter filename with path:')

#open csv file

with open(csvfile, 'rb') as newfile: #examples found online didn't define 'rb' formatting option...i don't really see a difference
	readaline = csv.reader(newfile)
	for row in readaline:
		print row

#parse the file

#close the file
