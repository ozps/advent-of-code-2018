lines = [line.rstrip('\n') for line in open('in.txt')]
num2 = 0
num3 = 0
for x in lines:
    bk = {}
    for y in x:
        if y not in bk:
            bk[y] = 1
        else:
            bk[y] += 1
    check_num = bk.values()
    if 2 in check_num:
        num2 += 1
    if 3 in check_num:
        num3 += 1
print(num2*num3)
