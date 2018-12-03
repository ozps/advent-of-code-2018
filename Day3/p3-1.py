lines = [line.rstrip('\n') for line in open('in.txt')]
s = [[0 for j in range(1005)] for i in range(1005)]
for x in lines:
    l = int(x[x.find('@')+2:x.find(',')])
    t = int(x[x.find(',')+1:x.find(':')])
    w = int(x[x.find(':')+2:x.find('x')])
    h = int(x[x.find('x')+1:])
    # print(l, t, w, h)
    for i in range(h):
        for j in range(w):
            if s[t+i][l+j] == 0:
                s[t+i][l+j] = 1
            elif s[t+i][l+j] == 1:
                s[t+i][l+j] = 2
# for i in range(10):
#     print()
#     for j in range(10):
#         print(s[i][j], end='')
i_w = 0
for i in range(1005):
    for j in range(1005):
        if s[i][j] == 2:
            i_w += 1
print(i_w)
