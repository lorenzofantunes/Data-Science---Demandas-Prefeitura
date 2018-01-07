import csv

with open('demandas.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    data = list(spamreader)

    for x in range(0, 5):
        data[x] = [x.replace(";", "").rstrip() for x in data[x]]
        print(str(data[x]) + "\n")
