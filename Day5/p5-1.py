lines = [line.rstrip('\n') for line in open('in.txt')]
i = 0
l = len(lines[0])-1
while(i != l and i <= l):
    if abs(ord(lines[0][i])-ord(lines[0][i+1])) == 32:
        #print(lines[0][:i], lines[0][i+2:], i)
        lines[0] = lines[0][:i]+lines[0][i+2:]
        # print(lines[0])
        i -= 2
        l -= 2
        if i <= 0:
            i = -1
        # print(len(lines[0]))
    i += 1
print(lines[0], len(lines[0]))
