__author__ = 'Dell'

import csv
from datetime import datetime

# import matplotlib
# matplotlib.use('ps')
import matplotlib.pyplot as plt
import numpy as np

startreader = csv.reader(open("start-fav-indegree.csv", "r"), delimiter='\t')
endreader = csv.reader(open("end-fav-indegree.csv", "r"), delimiter='\t')

base = datetime.strptime('2006-11-02', "%Y-%m-%d")
end = datetime.strptime('2007-05-18', "%Y-%m-%d")

num = (end-base).days+1

startdegrees = []

enddegree = dict((int(row[0]), int(row[1])) for row in endreader)

y = []

for row in startreader:
    startdegrees.append(int(row[1]))
    y.append(float(enddegree[int(row[0])]-int(row[1]))/float(num))

numbins = np.array(startdegrees).max()

print numbins

n, binlist = np.histogram(startdegrees, bins=numbins)
sy, _ = np.histogram(startdegrees, bins=numbins, weights=y)

plotx = []
mean = []

for i in xrange(len(n)):
    if n[i] == 0 or sy[i] == 0:
        continue
    else:
        meanval = float(sy[i])/float(n[i])
        # pref_fav1
        # if i+1 >= 699 and i+1 <= 35000 and meanval >= 0.001 and meanval <= 0.32:
        #     continue
        # else:
        # pref_fav2
        # if i+1 >= 370 and i+1 <= 10000 and meanval >= 0.001 and meanval <= 0.16:
        #     continue
        # else:
        # pref_rec2
        if i+1 >= 300 and i+1 <= 1000 and meanval >= 0.001 and meanval <= 0.16:
            continue
        else:
            mean.append(float(sy[i])/float(n[i]))
            plotx.append(i+1)

plt.grid()
plt.xlabel('Favorite Indegree (bin)')
plt.ylabel('Initiating Favorites Received (new user favorites/user/day)')
plt.loglog(plotx, mean, '+')
plt.show()
# plt.savefig('pref_rec2.eps', format='eps', dpi=1000)
