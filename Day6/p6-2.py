lines = [line.rstrip('\n') for line in open('in.txt')]
x = []
y = []
count = 0
for item in lines:
    x.append(int(item[:item.find(',')]))
    y.append(int(item[item.find(' ')+1:]))
max_all = max(x) if max(x) < max(y) else max(y)
bk = [[-1 for j in range(max_all+2)] for i in range(max_all+2)]
for i in range(max_all+2):
    for j in range(max_all+2):
        sum_mht = 0
        for k in range(len(x)):
            sum_mht += abs(x[k]-j)+abs(y[k]-i)
        if sum_mht < 10000:
            count += 1
print(count)
