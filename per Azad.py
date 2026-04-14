a = int(input())
max = float("-inf")
min = float("+inf")
while a > 0:
    k = a % 10
    a = a // 10
    if max < k:
        max = k
    if min > k:
        min = k
if max == min:
    if max != 9 and max != 8:
        print(9*100 + 8*10 + max)
    else:
        print(9*100 + 8*10 + 7)
else:
    print(9*100 + max*10 + min)
