# read in trained data
n = input()
N = int(n)
dataset = []
for i in range(N):
    line = input().rstrip().split(' ')
    ss = len(line)
    tmp = int(line[0])
    for j in range(1,ss):
        line[j-1] = int(line[j][-1])
    line[-1] = tmp
    dataset.append(line)

#read in test dataset
nn = input()
test_n = int(nn)
test = []
for i in range(test_n):
    ll = input().rstrip().split(' ')
    s = len(ll)
    for j in range(s):
        ll[j] = int(ll[j][-1])
    test.append(ll)

# Split a dataset based on an attribute and an attribute value
def test_split(index, value, dataset):
    left, right = list(), list()
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    # count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))
    # sum weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))
        # avoid divide by zero
        if size == 0:
            continue
        score = 0.0
        # score the group based on the score for each class
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        # weight the group score by its relative size
        gini += (1.0 - score) * (size / n_instances)
    return gini

# Select the best split point for a dataset
def get_split(dataset):
    # how to split when dataset is large? calculate gini index?
    b_index, b_value, b_score, b_groups = 999, 999, 0.742, None
    # if(len(dataset)>1000):
    #    return {'index':b_index, 'value':b_value, 'groups':b_groups}
    class_values = list(set(row[-1] for row in dataset))
    for index in range(len(dataset[0])-1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
                return {'index':b_index, 'value':b_value, 'groups':b_groups}

# Create a terminal node value
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])
    # print(node,'node 0')
    # check for a no split
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        # print(node,'node terminate')
        return
    # check for max depth and min size
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        # print(node,'node max depth')
        return
    # process left child
    if len(left) <= min_size:
        # print(node,'node left ter')
        node['left'] = to_terminal(left)
    else:
        # print(node,'node left split')
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth+1)
    # process right child
    if len(right) <= min_size:
        # print(node,'node right term')
        node['right'] = to_terminal(right)
    else:
        # print(node,'node right split')
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth+1)

# Make a prediction with a decision tree
def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

def decision_tree(train,test,max_depth,min_size):
    tree = get_split(train)
    split(tree,max_depth,min_size,0)
    predictions = []
    for row in test:
        prediction = predict(tree,row)
        predictions.append(prediction)
    return predictions
pre = decision_tree(dataset,test,3,25)
for p in pre:
    print(p)