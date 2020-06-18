# create empty dictionary

d = {}

text = open('reviews_sample.txt','r')
for lines in text:
	line = lines.strip().split(' ')
	tmp = set()
	for word in line:
		if word not in tmp:
			tmp.add(word)
	for t in tmp:
		if t not in d:
			d[t] = 1
		else:
			d[t]+=1
text.close()

def apriori_prune(ck,minsup):
	res = {}
	for i in ck:
		if ck[i] >= minsup:
			res[i] = ck[i]
	return res

minsup = 100
f1 = apriori_prune(d,minsup)


# print len-1 freq item to file
output = open('1-item.txt','w')
for f in f1:
	output.write(str(f1[f]))
	output.write(':')
	output.write(f)
	output.write('\n')
output.close()

# generate len-2 item sets
from itertools import permutations
def apriori_gen(fk,leng):
	res = []
	perm = permutations(fk,leng)
	for p in perm:
		res.append(p)
	return res
c2 = apriori_gen(f1,2)



# construct str for each element in c2
def contruct_freq_term(c2):
	res = []
	for c in c2:
		tmp = ""
		for i in c:
			tmp += i + ' '
		res.append(tmp[0:len(tmp)-1])
		tmp = ""
	return res
c2out = contruct_freq_term(c2)



# convert each line in input file into tuples add in token to avoid confusion
input_file = open('reviews_sample.txt','r')
tuple_of_lines = []
for lines in input_file:
	line = ';'+lines.strip().replace(' ',';')+';'
	t = str(line)
	tuple_of_lines.append(t)
input_file.close()



dout={}
for ou in c2out:
	ou = ';'+';'.join(ou.split())+';'
	for line in tuple_of_lines:
		if ou in line:
			if ou in dout:
				dout[ou] += 1
			else:
				dout[ou] = 1

res ={}
for i in dout:
	if dout[i] >= minsup:
		res[i] = dout[i]
print(res,'res')

two = open('res_two.txt','w')
for f in res:
	two.write(str(res[f]))
	two.write(':')
	two.write(f)
	two.write('\n')
two.close()






