from itertools import combinations 

import re

text_in = open('patterns2.txt')
dict_of_words = {}
set_of_two_word = []

for lines in text_in:
	word = ""
	for l in lines:
		if l.isdigit() or l == '[' or l == ':':
			pass
		else:
			if l == ' ':
				continue
			if l == ']' or l == ',':
				if word in dict_of_words:
					dict_of_words[word] += 1
				else:
					dict_of_words[word] = 1
				word = ""
			else:
				word += l
print(dict_of_words,'dow')

res = []
for w in dict_of_words:
	if dict_of_words[w] > 1:
		res.append(w)

# print(res,'res')
candi = open('cand.txt','w')
for i in res:
	candi.write(i)
	candi.write('\n')
candi.close()

# for lines in text_in:
# 	item = ""
# 	for l in lines:
# 		if l.isdigit() or l == '[' or l == ':':
# 			continue
# 		else:
# 			item += l
# 			if l == ']':
# 				item = item[0:len(item)-2]
# 				if item not in set_of_two_word:
# 					set_of_two_word.append(item)
# 				item = ""

# print(set_of_two_word,'so2w')
# text_in.close()

# extract uniq words from 2-item freq
text = open('patterns2.txt')
set_of_word = []
for lines in text:
	# line = lines.strip()
	word = ""
	for l in lines:
		# print(word,'word')
		if l.isalpha() or l == '&' or l == ' ' or l == ')' or l == '(':
			# print(l,'l')
			word += l
		elif l == ',':
			if word not in set_of_word:
				set_of_word.append(word)
			word = ""
	if word not in set_of_word:
		set_of_word.append(word)
text.close()

# print(set_of_word,'set_of_word')
uniq = []
for s in set_of_word:
	s = s.strip(' ')
	uniq.append(s)
# print(uniq,'uniq')

def apriori_gen(fk,len):
	l = []
	comb = combinations(fk,len)
	for i in comb:
		l.append(i)
	return l

c3 = apriori_gen(res,3)
print(c3,'c3')



# def Apriori_count_subset(fin,trans):
# 	tmp = {}
# 	for f in fin:
# 		for tran in trans:
# 			if set(tran) >= set(f):
# 				# print(f,'f')
# 				# print(tran,'tran')
# 				key = str(f)
# 				# print(key,'key')
# 				if key in tmp:
# 					tmp[key] += 1
# 				else:
# 					tmp[key] = 1
# 	return tmp

# valid_3_item = Apriori_count_subset(c3,fout)



# find l2 from database with f2
file = open('c.txt','r')
trans = []
for lines in file:
	line = lines.strip();
	trans.append(line)
sorted(trans)
# print(trans,'trans')
for i in trans:
	tuple(i)
file.close()

def convert_to_list(trans):
	a = []
	for tran in trans:
		l1 = tran.split(';')
		a.append(l1)
		# print(a,'a')
	return a
r = convert_to_list(trans)

# count for occurance of each k-len freq item in input file as trans
def Apriori_count_subset(fin,trans):
	tmp = {}
	for f in fin:
		for tran in trans:
			if set(tran) >= set(f):
				# print(f,'f')
				# print(tran,'tran')
				key = str(f)
				# print(key,'key')
				if key in tmp:
					tmp[key] += 1
				else:
					tmp[key] = 1
	return tmp
fin = Apriori_count_subset(c3,r)
print(fin,'fin')
