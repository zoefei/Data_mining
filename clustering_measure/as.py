from sys import stdin
from collections import Counter
import math
from itertools import combinations


# total number of pts
n = 0
dict_tc = {}
dict_ct = {}
for line in stdin:
    n += 1
    x,y = line.split()
    x,y = int(x), int(y)
    if x not in dict_tc:
        dict_tc[x] = [y]
    else:
        dict_tc[x].append(y)
    if y not in dict_ct:
        dict_ct[y] = [x]
    else:
        dict_ct[y].append(x)
c_len = len(dict_ct)
t_len = len(dict_tc)


# construct the matrix
w = t_len
h = c_len
m = [[0 for x in range(w+1)] for y in range(h+1)] 
pm = [[0 for x in range(w+1)] for y in range(h+1)]

for d in dict_ct:
    for ct in dict_ct[d]:
        m[d][ct] += 1



# construct matrix, last col -> sum of each row, last row -> sum of each col
def entropy(m,flag):
    #  Ci sum, row sum
    H = 0
    res = []
    if flag == 0:
        sum_ci = []
        for i in range(h):
            ci = 0
            for j in range(w):
                ci += m[i][j]
            m[i][j+1] = ci
            sum_ci.append(ci)
        res = sum_ci
        # calcluate H(c)
        for s in sum_ci:
            H -= s/n*math.log(s/n)

    # Tj sum, col sum
    else:
        sum_tj = []
        for j in range(w):
            tj = 0
            for i in range(h):
                tj += m[i][j]
            m[i+1][j] = tj
            sum_tj.append(tj)
        res = sum_tj
        for s in sum_tj:
            H -= s/n*math.log(s/n)
    m[h][w] = n
    return H,res


hc,c_sum = entropy(m,0)
ht,t_sum = entropy(m,1)


def mutual(pm,m):
    I = 0
    for c in range(len(m)):
        for t in range(len(m[0])):
            pm[c][t] = m[c][t]/n
    for i in range(len(m)-1):
        for j in range(len(m[0])-1):
            if pm[i][j] != 0:
                I += pm[i][j]*math.log(pm[i][j]/(pm[-1][j]*pm[i][-1]))
    return I

I = mutual(pm,m)
NMI = round(I/math.sqrt(hc*ht),3)



def nCr(n,r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))

# tot pairs of points
N = nCr(n,2)

def TP(m):
    tmp = 0
    for i in range(len(m)-1):
        for j in range(len(m[0])-1):
            if m[i][j] > 2:
                tmp += nCr(m[i][j],2)
            elif m[i][j] == 2:
                tmp += 1
            else:
                continue
    return tmp
tp = TP(m)

def FP(c_sum,tp):
    tmp = 0
    for i in range(len(c_sum)):
        if c_sum[i] > 2:
            tmp += nCr(c_sum[i],2)
        elif c_sum[i] == 2:
            tmp += 1
        else:
            continue
    return tmp - tp

def FN(t_sum,tp):
    tmp = 0
    for i in range(len(t_sum)):
        if t_sum[i] > 2:
            tmp += nCr(t_sum[i],2)
        elif t_sum[i] == 2:
            tmp += 1
        else:
            continue
    return tmp - tp

print('%.3f' % (NMI),'%.3f' % (jac))