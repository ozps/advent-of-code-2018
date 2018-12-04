lines = [line.rstrip('\n') for line in open('in.txt')]
lines = sorted(lines)
g = {}
fall = -1
wake = -1
now_g = ''
for x in lines:
    if x[x.find(']')+2:x.find(']')+3] == 'G':
        if x[x.find('#')+1:x.find('b')-1] not in g:
            g[x[x.find('#')+1:x.find('b')-1]] = [0 for i in range(60)]
            now_g = x[x.find('#')+1:x.find('b')-1]
        else:
            now_g = x[x.find('#')+1:x.find('b')-1]
    elif x[x.find(']')+2:x.find(']')+3] == 'f':
        if x[x.find(':')-2:x.find(':')] != '00':
            fall = 0
        else:
            fall = int(x[x.find(':')+1:x.find(']')])
    elif x[x.find(']')+2:x.find(']')+3] == 'w':
        if x[x.find(':')-2:x.find(':')] != '00':
            wake = 0
        else:
            wake = int(x[x.find(':')+1:x.find(']')])
    if fall != -1 and wake != -1:
        for i in range(fall, wake):
            g[now_g][i] += 1
        fall = -1
        wake = -1
max_freq = 0
max_g = ''
for x in g:
    if max(g[x]) > max_freq:
        max_freq = max(g[x])
        max_g = x
min_g = 0
print("ID:", max_g)
for x in g:
    if x == max_g:
        for i in range(len(g[x])):
            if g[x][i] == max(g[x]):
                print("Min.", i, "Freq.", max(g[x]))
                min_g = i
                break
print(int(max_g)*min_g)
