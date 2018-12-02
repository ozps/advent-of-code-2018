lines = [line.rstrip('\n') for line in open('in.txt')]
s1 = ''
s2 = ''
ans = ''
for x in lines:
    if s1 != '':
        break
    else:
        for y in lines:
            count = 0
            if x != y:
                for i in range(len(x)):
                    if x[i] != y[i]:
                        count += 1
                if count == 1:
                    s1 = x
                    s2 = y
                    break
for i in range(len(s1)):
    if s1[i] == s2[i]:
        ans += s1[i]
print(ans)
