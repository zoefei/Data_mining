# create empty dictionary
d = {}
# open origianl text file for read
text = open('c.txt')
# main
for lines in text:
	line = lines.strip()
	for word in line.split(';'):
		if word in d:
			d[word] += 1
		else:
			d[word] = 1


MinSupport = 771
# create result text file to write into
f = open('patterns.txt', 'w')
def Apriori_prune(Ck,MinSupport):
	l = {}	
	for i in Ck:
		if Ck[i] > MinSupport:
			l[i] = Ck[i]
	return l

c1 = Apriori_prune(d,MinSupport)
# print 1-frequent items f1 to file
f1 = []
for i in c1:
	f1.append(i)
	f.write(str(c1[i]))
	f.write(':')
	f.write(i)
	f.write('\n')
f.close()

from itertools import combinations 
# Part 2
# Please write all the frequent category sets along with their absolute supports into a text file named "patterns.txt". 
# Every line corresponds to exactly one frequent category set and should be in the following format:
# support:category_1;category_2;category_3;...
# For example, suppose a category set (Fast Food; Restaurants) has an absolute support 2851, 
# then the line corresponding to this frequent category set in "patterns.txt" should be:
# 2851:Fast Food;Restaurants

def Apriori_gen(Fk,leng):
	l = []
	comb = combinations(Fk,leng)
	for i in comb:
		l.append(i)
	return l



def generate_candidates(L, k):
    """Generate candidate set from `L` with size `k`"""
    candidates = []
    for a in L:
        for b in L:
            res = a.union(b)
            if len(res) == k and a != b:
                candidates.add(res)
    return candidates
f2 = Apriori_gen(f1,2)


def convert_tuple_to_list(f2):
	res = []
	for f in f2:
		tmp = []
		for i in range(len(f)):
			tmp.append(f[i])
		res.append(tmp)
	return res
f3 = convert_tuple_to_list(f2)



# find l2 from database with f2
file = open('c.txt','r')
trans = []
for lines in file:
	line = lines.strip();
	trans.append(line)
sorted(trans)

for i in trans:
	tuple(i)
file.close()

def convert_to_list(trans):
	a = []
	for tran in trans:
		l1 = tran.split(';')
		a.append(l1)
	return a
res = convert_to_list(trans)



# count for occurance of each k-len freq item in input file as trans
def Apriori_count_subset(fin,trans):
	tmp = {}
	for f in fin:
		for tran in trans:
			if set(tran) >= set(f):
				key = str(f)
				if key in tmp:
					tmp[key] += 1
				else:
					tmp[key] = 1
	return tmp
fin = Apriori_count_subset(f3,res)
fout = Apriori_prune(fin,MinSupport)
print(fout,'fout')
text.close()
