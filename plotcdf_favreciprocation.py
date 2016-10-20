__author__ = 'Dell'

import csv
import matplotlib.pyplot as plt
import numpy as np

reader = csv.reader(open("fav-reciprocation.csv", "r"), delimiter='\t')

elapsedtime = []

for row in reader:
    # if float(row[2]) < 30.0:
        elapsedtime.append(float(row[2]))

print len(elapsedtime)

sorted_data = np.sort(elapsedtime)
yvals = np.arange(len(sorted_data))/float(len(sorted_data))
plt.xlim([0, 160])
plt.xlabel('Time to Reciprocate Initiating Favorite (days)')
plt.ylabel('CDF')
plt.grid()
plt.plot(sorted_data, yvals)
plt.show()
plt.savefig('initfavreciprocate_cdf.eps')

# num_bins = 20
# counts, bin_edges = np.histogram(elapsedtime, bins=num_bins, normed=True)
# cdf = np.cumsum(counts)
# plt.plot(bin_edges[1:], cdf)
# plt.show()
