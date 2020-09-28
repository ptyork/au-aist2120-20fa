steps = 0
swaps = 0
ls = [5,2,6,3,1,4,8,7]

for i in range(len(ls)):
    for j in range(i + 1, len(ls)):
        steps += 1
        if ls[i] > ls[j]:
            swaps += 1
            v = ls[i]
            ls[i] = ls[j]
            ls[j] = v

print(ls,steps,swaps)


ls = [5,2,6,3,1,4,8,7]
swapped = True
steps = 0
swaps = 0
while swapped:
    swapped = False
    for i in range(len(ls)-1):
        steps += 1
        if ls[i] > ls[i+1]:
            v = ls[i]
            ls[i] = ls[i+1]
            ls[i+1] = v
            swapped = True
            swaps += 1

print(ls,steps,swaps)


ls = [5,2,6,3,1,4,8,7]
steps = 0
swaps = 0
for i in range(0, len(ls)-1):
    low = ls[i]
    lowi = i
    for j in range (i+1, len(ls)):
        steps += 1
        if ls[j] < low:
            low = ls[j]
            lowi = j
    if i != lowi:
        v = ls[i]
        ls[i] = ls[lowi]
        ls[lowi] = v
        swaps += 1

print(ls,steps,swaps)
