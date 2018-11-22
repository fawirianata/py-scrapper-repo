import csv

with open('hasil.csv',mode='r') as csv_file:
	csv_reader = csv.reader(csv_file,delimiter=';')
	
	for line in csv_reader:
            linkDownload=line[0]
            namafile=line[3]
            download='wget --no-check-certificate -O '+namafile.lstrip()+' \"'+linkDownload+'\"'
            print(download)