__author__ = 'Dell'

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

startlinkreader = csv.reader(open("start-link-indegree.csv", "r"), delimiter='\t')
endlinkreader = csv.reader(open("end-link-indegree.csv", "r"), delimiter='\t')

startfavreader = csv.reader(open("start-fav-indegree.csv", "r"), delimiter='\t')

# endfavreader = csv.reader(open("end-fav-outdegree.csv", "r"), delimiter='\t')

base = datetime.strptime('2006-11-02', "%Y-%m-%d")
end = datetime.strptime('2007-05-18', "%Y-%m-%d")

num = (end-base).days+1

startdict = dict((int(row[0]), int(row[1])) for row in startlinkreader)
enddict = dict((int(row[0]), int(row[1])) for row in endlinkreader)

# startfavdict = dict((int(row[0]), int(row[1])) for row in startfavreader)
# endfavdict = dict((int(row[0]), int(row[1])) for row in endfavreader)

x = []
y = []

for row in startfavreader:

    try:
        startdeg = startdict[int(row[0])]
    except KeyError:
        startdeg = 0

    try:
        enddeg = enddict[int(row[0])]
    except KeyError:
        enddeg = 0

    if startdeg == enddeg == 0:
        print row[2]
        continue

    x.append(int(row[1]))
    y.append(float(enddeg-startdeg)/float(num))

numbins = np.array(x).max()

# print numbins

n, binlist = np.histogram(x, bins=numbins)
sy, _ = np.histogram(x, bins=numbins, weights=y)

plotx = []
mean = []

for i in xrange(len(n)):
    if n[i] == 0 or sy[i] == 0:
        continue
    else:
        mean.append(float(sy[i])/float(n[i]))
        plotx.append(i+1)


# plt.plot(x, y, '+')
# plt.loglog(x, y, '+')
# plt.plot(plotx, mean, '+')
plt.loglog(plotx, mean, '+')
plt.show()
