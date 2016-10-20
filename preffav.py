__author__ = 'Dell'

import csv
from datetime import datetime

favoritesreader = csv.reader(open("flickr-all-photo-favorite-markings.txt", "r"), delimiter='\t')
photosreader = csv.reader(open("flickr-all-photos.txt", "r"), delimiter = '\t')

photo_owner = dict((int(row[0]),int(row[2])) for row in photosreader)

infavgraph = dict()
outfavgraph = dict()

def write_file(input):
    inwriter = csv.writer(open(input[0], "wb"), delimiter='\t')
    outwriter = csv.writer(open(input[1], "wb"), delimiter='\t')

    for row in infavgraph:
        inwriter.writerow([row, len(set(infavgraph[row])), len(infavgraph[row])]) # id, number of in-favoriters, number of favs recd

    for row in outfavgraph:
        outwriter.writerow([row, len(set(outfavgraph[row])), len(outfavgraph[row])]) # id, number of ppl faved, number of favs given


base = datetime.strptime('2006-11-02', "%Y-%m-%d")
# end = datetime.strptime('2007-05-18', "%Y-%m-%d").date()

flag = 0

for row in favoritesreader:
    if flag == 0 and datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S") > base:
        flag = 1
        write_file(["start-fav-indegree.csv", "start-fav-outdegree.csv"])

    if photo_owner[int(row[1])] in infavgraph:
        infavgraph[photo_owner[int(row[1])]].append(int(row[0]))
    else:
        infavgraph[photo_owner[int(row[1])]] = [int(row[0])]

    if int(row[0]) in outfavgraph:
        outfavgraph[int(row[0])].append(photo_owner[int(row[1])])
    else:
        outfavgraph[int(row[0])] = [photo_owner[int(row[1])]]


write_file(["end-fav-indegree.csv", "end-fav-outdegree.csv"])
