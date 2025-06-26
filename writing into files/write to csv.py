# IMPORTINGS
import csv

# READING DATA
schema1 = ['empid', 'empname', 'empaddress']
data = [['11', 'john snow', 'winterfell'],
        ['12', 'ser jorah', 'kigslanding'],
        ['13', 'jeremy lannister', 'kigslanding']
        ]

# LOGIC
with open('employees.csv', 'w', newline='') as csvfile:
    empwriter = csv.writer(csvfile)
    empwriter.writerow(schema1)
    empwriter.writerows(data)
