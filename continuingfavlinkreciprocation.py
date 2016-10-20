
import csv
from datetime import datetime

edgesreader = csv.reader(open("flickr-growth-sorted.txt", "r"), delimiter='\t')
favoritesreader = csv.reader(open("flickr-all-photo-favorite-markings.txt", "r"), delimiter='\t')
photosreader = csv.reader(open("flickr-all-photos.txt", "r"), delimiter = '\t')

writer = csv.writer(open("KG-continuing-fav-link-reciprocation.csv", "wb"), delimiter='\t')

photo_owner = dict((int(row[0]), int(row[2])) for row in photosreader)

favorites = dict()
graph = dict()

for row in edgesreader:
    if int(row[1]) in graph:
        graph[int(row[1])].append((int(row[0]), datetime.strptime(row[2],"%Y-%m-%d")))
    else:
        graph[int(row[1])] = [(int(row[0]), datetime.strptime(row[2],"%Y-%m-%d"))]

for row in favoritesreader: # NOTE: the lists will have dates sorted in ascending order because the file's in that order
    src = int(row[0])
    dest = photo_owner[int(row[1])]

    if (src, dest) not in favorites:
        favorites[(src, dest)] = [datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")]
    else:
        favorites[(src, dest)].append(datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S"))

iter = 0

for src, dest in favorites:

    favdates = favorites[(src, dest)]

    for index in xrange(len(favdates)):
        if index == 0:
            continue
        else:
            try:
                for linksrc, linkdate in graph[src]:
                    if linksrc == dest:
                        if linkdate > favdates[index]:
                            difference = linkdate - favdates[index]
                            days = difference.days
                            seconds = difference.seconds

                            writer.writerow([src, dest, float(days) + float(seconds)/86400.0])

                        break

            except KeyError:
                iter += 1

print iter
