#!/usr/bin/python3

"""Produces good results for euclidic distances and many teams"""

__author__ = "Alexander Kain"
__copyright__ = "Copyright 2013"
__license__ = "cc by-sa 3.0"
__version__ = "0.0.0"
# https://stats.stackexchange.com/a/77457

def eqsc(X, K=None, G=None):
    "equal-size clustering based on data exchanges between pairs of clusters"
    from scipy.spatial.distance import pdist, squareform
    from matplotlib import pyplot as plt
    from matplotlib import animation as ani
    from matplotlib.patches import Polygon
    from matplotlib.collections import PatchCollection
    def error(K, m, D):
        """return average distances between data in one cluster, averaged over all clusters"""
        E = 0
        for k in range(K):
            i = numpy.where(m == k)[0] # indeces of datapoints belonging to class k
            E += numpy.mean(D[numpy.meshgrid(i,i)])
        return E / K
    numpy.random.seed(0) # repeatability
    N, n = X.shape
    if G is None and K is not None:
        G = N // K # group size
    elif K is None and G is not None:
        K = N // G # number of clusters
    else:
        raise Exception('must specify either K or G')
    D = squareform(pdist(X)) # distance matrix
    m = numpy.random.permutation(N) % K # initial membership
    E = error(K, m, D)
    # visualization
    #FFMpegWriter = ani.writers['ffmpeg']
    #writer = FFMpegWriter(fps=15)
    #fig = plt.figure()
    #with writer.saving(fig, "ec.mp4", 100):
    t = 1
    while True:
        E_p = E
        for a in range(N): # systematically
            for b in range(a):
                m[a], m[b] = m[b], m[a] # exchange membership
                E_t = error(K, m, D)
                if E_t < E:
                    E = E_t
                    print("{}: {}<->{} E={}".format(t, a, b, E))
                    #plt.clf()
                    #for i in range(N):
                        #plt.text(X[i,0], X[i,1], m[i])
                    #writer.grab_frame()
                else:
                    m[a], m[b] = m[b], m[a] # put them back
        if E_p == E:
            break
        t += 1
    fig, ax = plt.subplots()
    patches = []
    for k in range(K):
        i = numpy.where(m == k)[0] # indeces of datapoints belonging to class k
        x = X[i]
        patches.append(Polygon(x[:,:2], True)) # how to draw this clock-wise?
        u = numpy.mean(x, 0)
        plt.text(u[0], u[1], k)
    p = PatchCollection(patches, alpha=0.5)
    ax.add_collection(p)
    plt.show()

if __name__ == "__main__":
    import numpy
    from pprint import pprint
    N, n = 100, 2

    # Location data as list of x,y coordinates or Gauss Kruger
    # This generates sample data
    X = numpy.random.rand(N, n)

    # FIXME Actual production data
    # X = []
    # # Normalize data if needed
    # for gk in X:
    #     gk[0] /= 10000000.0
    #     gk[1] /= 10000000.0
    # X = numpy.array(X)
    
    X = numpy.array(X)

    # equal size clustering
    eqsc(X, G=18)