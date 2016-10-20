__author__ = 'Dell'

import csv
from datetime import datetime

edgesreader = csv.reader(open("flickr-growth-sorted.txt", "r"), delimiter = '\t')

ingraph = dict()
outgraph = dict()

def write_edge_file(input):
    inwriter = csv.writer(open(input[0], "wb"), delimiter='\t')
    outwriter = csv.writer(open(input[1], "wb"), delimiter='\t')

    for row in ingraph:
        if len(ingraph[row]) != len(set(ingraph[row])):
            print "Something is wrong with the edges file"
        inwriter.writerow([row, len(ingraph[row])])

    for row in outgraph:
        if len(outgraph[row]) != len(set(outgraph[row])):
            print "Something is wrong with the edges file"
        outwriter.writerow([row, len(outgraph[row])])

base = datetime.strptime('2006-11-02', "%Y-%m-%d")
# end = datetime.strptime('2007-05-18', "%Y-%m-%d").date()

flag = 0

for row in edgesreader:
    if flag == 0 and datetime.strptime(row[2], "%Y-%m-%d") > base:
        flag = 1
        write_edge_file(["start-link-indegree.csv", "start-link-outdegree.csv"])

    if int(row[1]) in ingraph:
        ingraph[int(row[1])].append(int(row[0]))
    else:
        ingraph[int(row[1])] = [int(row[0])]

    if int(row[0]) in outgraph:
        outgraph[int(row[0])].append(int(row[1]))
    else:
        outgraph[int(row[0])] = [int(row[1])]

write_edge_file(["end-link-indegree.csv", "end-link-outdegree.csv"])
