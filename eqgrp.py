#!/usr/bin/python3

"""Produces good results for euclidic distances, but can't handle enough teams (~30)"""

from equal_groups_lib import EqualGroupsKMeans

import numpy as np

X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
# FIXME Actual production data

clf = EqualGroupsKMeans(n_clusters=2)

clf.fit(X)

print(clf.labels_)
