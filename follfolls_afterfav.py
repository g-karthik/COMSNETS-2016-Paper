__author__ = 'Dell'

import csv
from datetime import datetime
import datetime as dt

edgesreader = csv.reader(open("flickr-growth-sorted.txt", "r"), delimiter='\t')
favoritesreader = csv.reader(open("flickr-all-photo-favorite-markings.txt", "r"), delimiter='\t')
photosreader = csv.reader(open("flickr-all-photos.txt", "r"), delimiter = '\t')

graph = dict()

for row in edgesreader:
    if int(row[1]) in graph:
        graph[int(row[1])].append((int(row[0]), datetime.strptime(row[2],"%Y-%m-%d")))
    else:
        graph[int(row[1])] = [(int(row[0]), datetime.strptime(row[2],"%Y-%m-%d"))]

photo_owner = dict((int(row[0]),int(row[2])) for row in photosreader)
favorites = dict()

base = datetime.strptime('2006-11-02', "%Y-%m-%d").date()
end = datetime.strptime('2006-12-03', "%Y-%m-%d").date()
datelist = [end - dt.timedelta(days=x) for x in range(0, (end-base).days+1)]

base = datetime.strptime('2007-02-03', "%Y-%m-%d").date()
end = datetime.strptime('2007-05-18', "%Y-%m-%d").date()
datelist.extend(end - dt.timedelta(days=x) for x in range(0, (end-base).days+1))

dateset = set(datelist)

for row in favoritesreader:
    if datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S").date() in dateset:
        if photo_owner[int(row[1])] in favorites:
            favorites[photo_owner[int(row[1])]].append((int(row[0]), datetime.strptime(row[2],"%Y-%m-%d %H:%M:%S")))
        else:
            favorites[photo_owner[int(row[1])]] = [(int(row[0]), datetime.strptime(row[2],"%Y-%m-%d %H:%M:%S"))]

del photo_owner

writer = csv.writer(open("future-follows.csv", "wb"), delimiter='\t')

for dest in favorites:
    for src, favdate in favorites[dest]:
        srcfoll = []

        try:
            graph[src]
        except KeyError:
            print "KeyError in graph[src]"
            continue

        for foll, folldate in graph[src]:
            if folldate <= favdate:
                srcfoll.append(foll)

        destfoll = []

        try:
            for foll, folldate in graph[dest]:
                if folldate <= favdate:
                    destfoll.append(foll)
        except KeyError:
            print "KeyError in graph[dest]"

        twohopfoll = set(srcfoll)-set(destfoll)

        totalfollcount = 0
        twohopfollcount = 0
        converts = set()

        try:
            for foll, folldate in graph[dest]:
                if folldate > favdate:
                    totalfollcount += 1
                    if foll in twohopfoll:
                        twohopfollcount += 1
                        converts.add(foll)
        except KeyError:
            print "KeyError in graph[dest] - 2"

        try:
            percentage = float(len(converts))/float(len(twohopfoll))
        except ZeroDivisionError:
            percentage = 0.0

        writer.writerow([dest, len(destfoll), src, len(srcfoll), totalfollcount, twohopfollcount, len(twohopfoll),
                         percentage])

