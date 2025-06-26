import csv

outputlist = []

with open('employees.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        print(i['empid'], i['empname'], i['empaddress'])
        outputlist.append(i.values())

    print(outputlist)

