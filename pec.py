import itertools as it
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

def pec(y, D, t):
    y_len = len(y)
    serial = np.arange(0, D)
    y_perm = list(it.permutations(serial, D))
    count = np.zeros(len(y_perm))
    '''for item in y_perm:
        print(item)
    '''

    for i in range(y_len-(D-1)*t):
        y_x = np.argsort(y[i:i+t*D:t])
        #print(tuple(y_x))

        for j in range(len(y_perm)):
            if tuple(y_x) == y_perm[j]:
                count[j] += 1

    #plt.hist(count)
    #plt.show()

    pe = scipy.stats.entropy(count / (y_len-(D-1)*t), base=2)
    #print(pe)
    return pe

'''
D = 3, t = 1
Partition:
[[ 4,  7,  9, 10,  6]
 [ 7,  9, 10,  6, 11]
 [ 9, 10,  6, 11,  3]]
 
 [ 4,  7,  9]->[0, 1, 2]
 [ 7,  9, 10]->[0, 1, 2]
 [ 9, 10,  6]->[2, 0, 1]
 [10,  6, 11]->[1, 0, 2]
 [ 6, 11,  3]->[2, 0, 1]
 
 pe = -∑pi*log(pi) = -(2/5*log2(2/5) + 1/5*log2(1/5) + 2/5*log2(2/5)) = 1.5219
'''


def test():
    y = [4, 7, 9, 10, 6, 11, 3]
    pec(y, 3, 1)
