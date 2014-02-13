#no more cheating
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", type=file)
#parser.add_argument("col", type=int)
args = parser.parse_args()
#create a table or matrix from file.csv

for row in args.file:
#	x = args.col - 1
	print row
