#!/usr/bin/python3

"""Produces clusters with short distances but of different size"""

# import all the things

## import sys stuff
import timeit
import logging
from pprint import pprint
import sys
import json

## import math stuff
from collections import Counter
import random

## import numeric stuff
from equal_groups import EqualGroupsKMeans
import numpy as np
from sklearn import cluster, datasets, mixture

# record runtime
start = timeit.default_timer()

# euclidian distance
def distance(c1,c2):
    x1 = float(c1[0])
    y1 = float(c1[1])
    x2 = float(c2[0])
    y2 = float(c2[1])
    return ((x1-x2)**2+(y1-y2)**2)**0.5

# data
## simple data
teams = np.array([
    [10, 10], [2, 1], [1, 0], [14, 26], [22, 11], [14, 58], [46, 24], [24, 12], [11, 34], [5, 0]
])

## random data
# grid = [(x,y) for x in range(20) for y in range(20)]
# X = random.sample(grid, 20)

## sample data
# teams = FIXME Actual production data

# config
clusters = 3
cluster_min = 6
cluster_max = 7

# run spectral first
clustering = cluster.SpectralClustering(
    n_clusters = clusters,
    assign_labels = "discretize",
    random_state = 0)
clustering.fit(teams)
divisions = dict(Counter(clustering.labels_))
print("Completed spectral clustering, distribution: " + str(divisions))

# convert all the stuff to lists, because numpy
teams = np.array(teams).tolist()
labels = np.array(clustering.labels_).tolist()

labels = [[i] for i in labels]
for key, team in enumerate(teams):
    team += labels[key]

print("Created lists, association to divisions: " + str(teams))

divisions_done = {}
divisions_todo = {}

print(divisions)
for index,numteams in divisions.items():
    if numteams >= cluster_min & numteams <= cluster_max:
        divisions_done[index] = numteams
    else:
        divisions_todo[index] = numteams

#for index,numteams in divisions_todo[index].items():
    

distance ([0,0],[3,4])

pprint(divisions_done)
pprint(divisions_todo)

# for index,team in enumerate(teams):
#     print (str(index) + ":" + str(clustering.labels_[index]))
#     a = np.concatenate(
#         team,
#         np.array(clustering.labels_[index])
#     )
#     print (a)
#     #teams_new.append()



# for cluster_key,cluster_teamcount in new_list:
#     if cluster_teamcount > cluster_max:
#         for team in X:
#             pprint(team)
#     print(str(cluster_key) + ":" + str(cluster_teamcount))

print('========== EXIT')

end = timeit.default_timer()
print('exec time '+ str(end - start))