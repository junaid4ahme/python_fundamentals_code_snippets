# count the number of lines in python file.

with open(file1, 'r') as fp:
    count = len(fp.readlines())

cnt = 0
for i in fileprop:
    cnt = cnt + 1

# HOW TO READ PYTHON FILE LINE BY LINE:
cnt = 0
with open(file1, 'r') as fp:
    lines = fp.readlines()

for i in lines:
    cnt = cnt + 1
    print(cnt, i.strip())

