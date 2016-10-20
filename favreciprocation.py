__author__ = 'Dell'


##
## init fav must be the first fav from src to dest
## reciprocated fav must be the first fav from dest to src
## reciprocated fav must have larger timestamp than init fav
##


import csv
from datetime import datetime

edgesreader = csv.reader(open("flickr-growth-sorted.txt", "r"), delimiter='\t')
favoritesreader = csv.reader(open("flickr-all-photo-favorite-markings.txt", "r"), delimiter='\t')
photosreader = csv.reader(open("flickr-all-photos.txt", "r"), delimiter = '\t')

writer = csv.writer(open("fav-reciprocation.csv", "wb"), delimiter='\t')

photo_owner = dict((int(row[0]), int(row[2])) for row in photosreader)
favorites = dict()

for row in favoritesreader: # all-photo-favorite-markings is sorted in ascending order of favorite time, code depends on that
        if (photo_owner[int(row[1])], int(row[0])) not in favorites:
            favorites[(photo_owner[int(row[1])], int(row[0]))] = datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")

for dest, src in favorites:

    initdate = favorites[(dest, src)]
    try:
        reciprocatedate = favorites[(src, dest)]
    except KeyError:
        print "No favorite reciprocation"
        continue

    if reciprocatedate > initdate:
        difference = reciprocatedate-initdate
        days = difference.days
        seconds = difference.seconds

        writer.writerow([src, dest, float(days) + float(seconds)/86400.0])
