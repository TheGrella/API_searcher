import csv
from time import time
from os.path import isfile, join, isdir
from unittest import skip

ids = []
count = 0


for i in range(1,30):
    try:
        file = open('./temporanea/Api_total'+str(i)+'.csv')
        csvreader = csv.reader(file)

        for row in csvreader:
            if row[0] not in ids:
                ids.append(row[0])

                with open('Final_API.csv', 'a', encoding='UTF8') as outfile:
                    writer = csv.writer(outfile)
                    writer.writerow(row)
            else:
                count += 1 
        file.close()
    except:
        skip
print("Doppioni: " + str(count))