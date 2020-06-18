from itertools import combinations 

text = open('cand.txt','r')
res = []
for lines in text:
	line = lines.strip()
	res.append(line)



def apriori_gen(fk,len):
	l = []
	comb = combinations(fk,len)
	for i in comb:
		l.append(set(i))
	return l

c3 = apriori_gen(res,3)

c3_list = []
for c in c3:
	c3_list.append(c)



# find l2 from database with f2
file = open('c.txt','r')
trans = []
for lines in file:
	line = lines.strip();
	trans.append(line)
sorted(trans)



def convert_to_list(trans):
	a = []
	for tran in trans:
		l1 = tran.split(';')
		a.append(l1)
	return a
r = convert_to_list(trans)



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
fin = Apriori_count_subset(c3_list,r)
print(fin,'fin')



def Apriori_prune(Ck,MinSupport):
	l = {}	
	for i in Ck:
		if Ck[i] > MinSupport:
			l[i] = Ck[i]
	return l
finish = Apriori_prune(fin,771)
