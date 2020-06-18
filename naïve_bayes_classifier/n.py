from sys import stdin

n = input().split(',')
# print(n)
attr = n[1:-1]
# print(attr,'attr')
attr_len = len(attr)
# print(attr_len,'attr len')
data=[]
for line in stdin:
    data.append(line.rstrip())

split_data = [d.split(',') for d in data]
# print(split_data,'split')

# clean up dataset, separate out test remove first attribute animal name
dataset = []
test = []
for i in split_data:
    # print(i[-1])
    if i[-1] != '-1':
        dataset.append(i[1:])
    else:
        test.append(i[1:])
# print(dataset,'dataset')
# print(test,'test')
N = len(dataset)
n1 = len(dataset)+len(test)
# print(N,'N')

# get class types from dataset
class_types = set()
for d in dataset:
    class_types.add(d[-1])
# print(class_types,'class_types')

# separate Ci
def sep_ci(dataset,class_types):
    c_i = dict()
    for i in range(N):
        val = dataset[i]
        k = dataset[i][-1]
        if k not in c_i:
            c_i[k] = list()
        c_i[k].append(val)
    return c_i
# data = dataset+test
# print(data,'data')
ci = sep_ci(dataset,class_types)
# print(ci,'ci')

# calculate P(Ci)
def cal_pci(label):
    # print(len(label),'len label')
    deno = len(label)+0.1
    # print(deno,'deno')
    nom = N+0.1*len(class_types)
    # print(nom,'nom')
    return deno/nom

attr_vec = []
for t in test:
    attr_vec.append(t[:-1])
# print(attr_vec,'attr_vec')

# calculate P(x|ci)
def cal_pxci(val,ti):
    p = 1
    deno = 0
    nom = 0
    para = 0.2
    # for v in val:
    #     tmp = 0
    #     for i in range(len(ti)):
    # print(len(val),'val len')
    for i in range(len(ti)-1):
        tmp = 0
        for v in val:
            # tmp = 0
            if i == 12:
                para = 0.6
            if v[i] == ti[i]:
                # if i == 12:
                #     para = 0.6
                tmp += 1
            # print(tmp,'tmp')
        deno = tmp+0.1
        # print(deno,'deno')
        nom = len(val)+para
        # print(nom,'nom')
        p *= (deno/nom)
    return p

def cal_by_class(cci,ti):
    # print(cci,'cci')
    res = []
    for key, val in cci.items():
        # print(key,'key')
        # print(val,'val')
        pxy = cal_pxci(val,ti)
        # print(pxy,'pxy')
        py = cal_pci(val)
        # print(py,'py')
        res.append(((pxy*py),key))
    # print(res,'res')
    return res

rr = []
for a in attr_vec:
    key = -3
    tmp = float('-inf')
    a_res = cal_by_class(ci,a)
    for i in a_res:
        # print(i[0],'i')
        if i[0] > tmp:
            # print(tmp,'tmp')
            # print(i[1],'i1')
            tmp = max(tmp,i[0])
            key = i[1]
    rr.append(key)
# print(rr,'rr')
for r in rr:
    print(r)
# print(rr,'rr')