##
## init fav must be the first fav from src to dest
##

import csv
from datetime import datetime

edgesreader = csv.reader(open("flickr-growth-sorted.txt", "r"), delimiter='\t')
favoritesreader = csv.reader(open("flickr-all-photo-favorite-markings.txt", "r"), delimiter='\t')
photosreader = csv.reader(open("flickr-all-photos.txt", "r"), delimiter = '\t')

writer = csv.writer(open("KG-fav-link-reciprocation.csv", "wb"), delimiter='\t')

photo_owner = dict((int(row[0]), int(row[2])) for row in photosreader)
favorites = dict()
graph = dict()

for row in edgesreader:
    if int(row[1]) in graph:
        graph[int(row[1])].append((int(row[0]), datetime.strptime(row[2],"%Y-%m-%d")))
    else:
        graph[int(row[1])] = [(int(row[0]), datetime.strptime(row[2],"%Y-%m-%d"))]

for row in favoritesreader: # all-photo-favorite-markings is sorted in ascending order of favorite time, code depends on that
        if (photo_owner[int(row[1])], int(row[0])) not in favorites:
            favorites[(photo_owner[int(row[1])], int(row[0]))] = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")

for dest, src in favorites:

    try:
        initdate = favorites[(dest, src)]

        for linksrc, linkdate in graph[src]:
            if linksrc == dest:
                if linkdate > initdate:
                    difference = linkdate - initdate
                    days = difference.days
                    seconds = difference.seconds

                    writer.writerow([src, dest, float(days) + float(seconds)/86400.0])
                break
    except KeyError:
        print "KeyError - this can happen, ignore this and let the program continue running"
        continue
