import math
info = input().rstrip()

N, K, M = info.split(' ')
N, K, M = int(N), int(K), int(M)
data_pts = []
clusters = []
for i in range(N):
    x,y = input().rstrip().split(' ')
    x,y = float(x), float(y)
    data_pts.append((x,y))
    clusters.append([(x,y)])
keys = data_pts
# print(data_pts)  
# calculate euclidean distance between two points
def euclidean_dist(p1,p2):
    res = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return res

# calculate the distance between clusters based on M
def cluster_dist(c1,c2,M):
    d0 = float('inf')
    d1 = float(0)
    dist_tot, pair = float(0), int(0)
    # single link, find min dist among two clusters
    if M == 0:
        for p1 in c1:
            for p2 in c2:
                d0 = min(d0,euclidean_dist(p1,p2))
                res = d0
    # complete link
    elif M == 1:
        for p1 in c1:
            for p2 in c2:
                d1 = max(d1,euclidean_dist(p1,p2))
                res = d1
    # avg link
    else:
        for p1 in c1:
            for p2 in c2:
                dist_tot += euclidean_dist(p1,p2)
                pair += 1
                res = dist_tot/pair
    return res
m1,m2 = 0,0
dict = {}
for k in keys:
    dict[k] = 0
print(dict,'dict')
while len(clusters) > K:
    # find idx for clusters to merge
    dist = float('inf')
    for i in range(len(clusters)):
        for j in range(i+1, len(clusters)):
            c_dist = cluster_dist(clusters[i],clusters[j],M)
            if c_dist < dist:
                dist = c_dist
                m1, m2 = i, j
    # print(clusters[m1],'m1')
    # print(clusters[m2],'m2')
    # merge two min dist clusters m1+m2 and remove m1, m2
    agglo = clusters[m1] + clusters[m2]
    # print(agglo,'agglo')
    clusters = clusters[:m1] + clusters[m1+1:m2] + clusters[m2+1:]
    clusters.append(agglo)
print(clusters,'cluser')
# for c,idx in enumerate(clusters):
i = 0
for cluster in clusters:
    print(cluster,'cluster')
    for c in cluster:
    # if c in cluster:
        dict[c] = i
    i += 1
print(dict,'final')
out = []
for d in dict:
    print(dict[d])s