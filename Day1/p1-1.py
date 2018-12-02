lines = [line.rstrip('\n') for line in open('in.txt')]
sum = 0
for x in lines:
    sum += int(x)
print(sum)
