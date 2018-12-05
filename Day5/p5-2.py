lines = [line.rstrip('\n') for line in open('in.txt')]
s = ''
new_lines = lines[0]
ans = []
for i in range(ord('a'), ord('z')+1):
    new_lines = new_lines.replace(chr(i), '')
    new_lines = new_lines.replace(chr(i-32), '')
    i = 0
    l = len(new_lines)-1
    while(i != l and i <= l):
        if abs(ord(new_lines[i])-ord(new_lines[i+1])) == 32:
            #print(new_lines[:i], new_lines[i+2:], i)
            new_lines = new_lines[:i]+new_lines[i+2:]
            # print(new_lines)
            i -= 2
            l -= 2
            if i <= 0:
                i = -1
        i += 1
    ans.append(len(new_lines))
    new_lines = lines[0]
print(sorted(ans)[0])
