from math import sqrt
import random
from decimal import Decimal
import copy


# use a map to store each id with its location
def read_input(text,size):
	list_of_places = [None]*size
	i = 0
	for lines in text:
		line = lines.strip()
		list_of_places[i] = line
		i += 1
	return list_of_places

def initial_clusters(size,list_of_places,k):
	# pick first centroid randomly
	c1,c2,c3 = random.sample(range(0,size-1), k)
	xa,ya = list_of_places[c1].split(',')
	xb,yb = list_of_places[c2].split(',')
	xc,yc = list_of_places[c3].split(',')

	xa = float(xa)
	ya = float(ya)
	xb = float(xb)
	yb = float(yb)
	xc = float(xc)
	yc = float(yc)

	cur_c0 = [xa,ya]
	cur_c1 = [xb,yb]
	cur_c2 = [xc,yc]
	return cur_c0,cur_c1,cur_c2

# calculate euclidean distance between two points
def euclidean_dist(xc,yc,x1,y1):
	res = sqrt((xc-x1)**2 + (yc-y1)**2)
	return res

# calculate and assign each line to a cluster
def cal_clusters(list_of_places, cur_c0, cur_c1, cur_c2,size):
	res_map = [None]*size
	for i,l in enumerate(list_of_places):
		lx,ly = l.split(',')
		lx = float(lx) 
		ly = float(ly)
		# compute distance from current point to three centroids
		d1 = euclidean_dist(cur_c0[0],cur_c0[1],lx,ly)
		d2 = euclidean_dist(cur_c1[0],cur_c1[1],lx,ly)
		d3 = euclidean_dist(cur_c2[0],cur_c2[1],lx,ly)

		min_val = min(min(d1,d2),d3)
		if min_val == d1:
			cluster = 0
		elif min_val == d2:
			cluster = 1
		else:
			cluster = 2
		# assign to closest cluster
		res_map[i] = cluster
	return res_map

# calculate new centroids for each cluster
def cal_centroids(res_map,list_of_places):
	cluster0 = []
	cluster1 = []
	cluster2 = []
	x_tol = 0
	y_tol = 0
	for index,r in enumerate(res_map):
		if r == 0:
			cluster0.append(list_of_places[index])
		elif r == 1:
			cluster1.append(list_of_places[index])
		else:
			cluster2.append(list_of_places[index])
	for c in cluster0:
		x,y = c.split(',')
		x = float(x)
		y = float(y)
		# print(x,'x0')
		x_tol += x
		y_tol += y
		x1 = x_tol/len(cluster0)
		y1 = y_tol/len(cluster0)
		# print(x1,'x1')
	x_tol = 0
	y_tol = 0
	for c in cluster1:
		x,y = c.split(',')
		x = float(x)
		y = float(y)
		x_tol += x
		y_tol += y
		x2 = x_tol/len(cluster1)
		y2 = y_tol/len(cluster1)
	x_tol = 0
	y_tol = 0
	for c in cluster2:
		x,y = c.split(',')
		x = float(x)
		y = float(y)
		x_tol += x
		y_tol += y
		x3 = x_tol/len(cluster2)
		y3 = y_tol/len(cluster2)
	return [[x1,y1],[x2,y2],[x3,y3]]



# print to output file
def print_output(res_map):
	#write to output file
	out = open('clusters.txt','w')
	for i,r in enumerate(res_map):
		out.write(str(i))
		out.write(' ')
		out.write(str(res_map[i]))
		out.write('\n')
	out.close()


def main():
	text = open('places.txt','r')
	size = 300 #length of the text file
	#read input from file
	list_of_places = read_input(text,size)
	text.close()
	# define number of loops
	max_loop = 100
	# define number of clusters
	k = 3

	centroids = initial_clusters(size,list_of_places,k)
	# print(init_clusters)
	
	loop = 1
	while loop <= max_loop:
		cluster = cal_clusters(list_of_places,centroids[0],centroids[1],centroids[2],size)
		# print(cluster,'cluster')
		# prev_centroids = copy.deepcopy(centroids)
		centroids = cal_centroids(cluster,list_of_places)
		new_cluster = cal_clusters(list_of_places,centroids[0],centroids[1],centroids[2],size)
		# print(new_cluster,'new cluster')
		loop += 1
	# print(new_cluster,'res')
	print_output(new_cluster)


if __name__ == "__main__":
	main()