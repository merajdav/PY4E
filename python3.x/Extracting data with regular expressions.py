import re
fh = open('regex_sum_613186.txt')
numlist = list()
for line in fh:
    stuff = re.findall('[0-9]+', line)
    if len(stuff) < 1:
        continue
    for anum in stuff:
        num = int(anum)
        numlist.append(num)
print(numlist)
print(sum(numlist))
