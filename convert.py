import sys
import csv
import os
from openpyxl import Workbook

files = os.listdir('CSV')
for file in files:
	root, ext = os.path.splitext(file)
	if '.csv' in ext:
		wb = Workbook()
		ws = wb.active
		with open('CSV/'+file) as csv_file:
			print('Processing File : '+root)
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
		    		ws.append(row)
		wb.save('XLSX/'+root+'.xlsx')