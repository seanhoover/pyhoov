#no more cheating
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="Needs Filename", type=argparse.FileType('r'))
parser.add_argument("--column", help="Printing Cols", action="store_true")
parser.add_argument("col#", type=int)
args = parser.parse_args()
if args.column:
	for row in args.file.readlines():
		print row["col#"]
