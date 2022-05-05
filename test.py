train = open("train.txt", 'r')
domain = dict()
for line in train.readlines():
    line = line.strip('\n')
    temp = line.split(',')
    domain[temp[0]] = temp[1]
length = 0
for i in domain.keys():
    if len(i) > length and domain[i] == "notdga":
        length = len(i)
train.close()

test = open("test.txt", 'r')
result = list()
for line in test.readlines():
    line = line.strip('\n')
    if len(line) > length + 1:
        result.append(line + ",dga\n")
    else:
        result.append(line + ",notdga\n")
test.close()

output = open("result.txt", 'w')
output.writelines(result)
output.close()
