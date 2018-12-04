lines = [line.rstrip('\n') for line in open('in.txt')]
lines = sorted(lines)
g = {}
fall = 0
now_g = ''
for x in lines:
    if x[x.find(']')+2:x.find(']')+3] == 'G':
        if x[x.find('#')+1:x.find('b')-1] not in g:
            g[x[x.find('#')+1:x.find('b')-1]] = 0
            now_g = x[x.find('#')+1:x.find('b')-1]
        else:
            now_g = x[x.find('#')+1:x.find('b')-1]
    elif x[x.find(']')+2:x.find(']')+3] == 'f':
        fall = int(x[x.find(':')+1:x.find(']')])
    elif x[x.find(']')+2:x.find(']')+3] == 'w':
        g[now_g] += int(x[x.find(':')+1:x.find(']')])-fall
sorted_g = sorted(g.items(), key=lambda kv: kv[1], reverse=True)
max_g = sorted_g[0][0]
print("ID:", max_g)
bk_g = [0 for i in range(60)]
fall = -1
wake = -1
for x in lines:
    if x[x.find(']')+2:x.find(']')+3] == 'G':
        now_g = x[x.find('#')+1:x.find('b')-1]
    elif x[x.find(']')+2:x.find(']')+3] == 'f' and now_g == max_g:
        fall = int(x[x.find(':')+1:x.find(']')])
    elif x[x.find(']')+2:x.find(']')+3] == 'w' and now_g == max_g:
        wake = int(x[x.find(':')+1:x.find(']')])
    if wake != -1 and fall != -1:
        # print(fall, wake)
        for i in range(fall, wake):
            bk_g[i] += 1
        fall = -1
        wake = -1
min_g = 0
for i in range(len(bk_g)):
    if bk_g[i] == max(bk_g):
        print("Min.", i)
        min_g = i
        break
print(int(max_g)*min_g)
