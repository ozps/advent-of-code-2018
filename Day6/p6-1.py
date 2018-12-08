lines = [line.rstrip('\n') for line in open('in.txt')]
x = []
y = []
for item in lines:
    x.append(int(item[:item.find(',')]))
    y.append(int(item[item.find(' ')+1:]))
max_all = max(x) if max(x) < max(y) else max(y)
bk = [[-1 for j in range(max_all+2)] for i in range(max_all+2)]
for i in range(max_all+2):
    for j in range(max_all+2):
        temp = []
        for k in range(len(x)):
            temp.append((abs(x[k]-j)+abs(y[k]-i), k))
        temp = sorted(temp, key=lambda tup: tup[0])
        if bk[i][j] == -1:
            bk[i][j] = temp[0][1]
print()
border = set()
border.add(-1)
border.add(-2)
for i in range(max_all+1):
    border.add(bk[i][0])
    border.add(bk[i][max_all+1])
    border.add(bk[max_all+1][i])
    border.add(bk[0][i])
ans = {}
for i in range(max_all+2):
    for j in range(max_all+2):
        if bk[i][j] not in border:
            if bk[i][j] not in ans:
                ans[bk[i][j]] = 1
            else:
                ans[bk[i][j]] += 1
print(sorted(ans.values(), reverse=True)[0])
