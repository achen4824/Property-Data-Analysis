import numpy as np
import csv

#import text into array
with open('realestatecom.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	for line in csv_reader:
	    print(line[2])
