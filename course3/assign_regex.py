import re

fname = raw_input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print "Invalid file name or file not found"
    exit()

lst = list()
for line in fhandle:
    numbers = re.findall("[0-9]+", line)
    if len(numbers) >= 1:
        for number in numbers:
            lst.append(number)

count = 0
total = 0
for number_str in lst:
    number_int = int(number_str)
    count = count + 1
    total = total + number_int

print count, total
