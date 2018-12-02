lines = [line.rstrip('\n') for line in open('in.txt')]
ch = set()
a = True
sum = 0
while(a):
    for x in lines:
        sum += int(x)
        if sum not in ch:
            ch.add(sum)
        else:
            print(sum)
            a = False
            break
