class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


names = list()
names.append("Oct 3 W1.txt")
names.append("Oct 3 W2.txt")
names.append("Oct 3 W3.txt")
names.append("Oct 3 W4.txt")

names.append("Oct 4 W1.txt")
names.append("Oct 4 W2.txt")
names.append("Oct 4 W3.txt")
names.append("Oct 4 W4.txt")

names.append("Oct 5 W1.txt")
names.append("Oct 5 W2.txt")
names.append("Oct 5 W3.txt")
names.append("Oct 5 W4.txt")

names.append("Oct 6 W1.txt")
names.append("Oct 6 W2.txt")
names.append("Oct 6 W3.txt")
names.append("Oct 6 W4.txt")

names.append("Oct 7 W1.txt")
names.append("Oct 7 W2.txt")
names.append("Oct 7 W3.txt")
names.append("Oct 7 W4.txt")

names.append("Oct 10 W1.txt")
names.append("Oct 10 W2.txt")
names.append("Oct 10 W3.txt")
names.append("Oct 10 W4.txt")

# for name in names:
    # fh = open("Raw Data/" + name)
fh = open("Raw Data/Oct 3 W1.txt")

points = list()

minX = 120
minY = 120
maxX = 0
maxY = 0

for line in fh:
    fragments = line.split(",")
    x = float(fragments[0])
    y = float(fragments[1])
    # point = Point(x, y)
    # points.append(point)
    minX = min(minX, x)
    minY = min(minY, y)
    maxX = max(maxX, x)
    maxY = max(maxY, y)

# print 'For:', name.split('.')[0]
print 'Min:', minX, minY
print 'Max:', maxX, maxY
fh.close()
