# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index = line.find(" ")
    number_str = line[index:].strip()
    number = float(number_str)
    total = total + number
    count = count + 1
print "Average spam confidence:", total / count
