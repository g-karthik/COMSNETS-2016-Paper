__author__ = 'Dell'

import csv
import matplotlib
#matplotlib.use('ps')
import matplotlib.pyplot as plt
import numpy as np

#reader = csv.reader(open("fav-reciprocation.csv", "r"), delimiter='\t')
#newreader = csv.reader(open("continuing-fav-reciprocation.csv", "r"), delimiter='\t')

reader = csv.reader(open("KG-fav-link-reciprocation.csv", "r"), delimiter='\t')
newreader = csv.reader(open("KG-continuing-fav-link-reciprocation.csv", "r"), delimiter='\t')

elapsedtime = []
newelapsedtime = []

for row in reader:
    # if float(row[2]) < 30.0:
        elapsedtime.append(float(row[2]))

for row in newreader:
    #newelapsedtime.append(float(row[0]))
    newelapsedtime.append(float(row[2]))

#print len(elapsedtime)
#print len(newelapsedtime)

sorted_data = np.sort(elapsedtime)
yvals = np.arange(len(sorted_data))/float(len(sorted_data))

new_sorted_data = np.sort(newelapsedtime)
newyvals = np.arange(len(new_sorted_data))/float(len(new_sorted_data))

#plt.xlim([0, 160])
#plt.xlabel('Time Taken to Create Reverse Favorite (days)')
plt.xlabel('Time Taken to Reciprocate Favorite with Link (days)')
plt.ylabel('CDF')
plt.grid()

res1, = plt.plot(sorted_data, yvals, label="Initiating Favorite")
res2, = plt.plot(new_sorted_data, newyvals, label="Continuing Favorite", ls='--')
legend_results = [res1]
legend_results.append(res2)

plt.legend(handles=legend_results, loc=4)
plt.show()
#plt.savefig('initvscontinuingfav-linkrec.eps', format='eps', dpi=1000)
