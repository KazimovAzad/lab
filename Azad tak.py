import random
a = [random.randint(-100, 101) for i in range(int(input()))]
list1 =[]
list2 =[]
list_um = []
def selection_sort(a):
    n = len(a)
    for i in range(n):
        i_min = i
        for j in range(i + 1, n):
            if a[j] > a[i_min]:
                i_min = j
        a[i], a[i_min] = a[i_min], a[i]
    return a
def selection_sort(a):
    n = len(a)
    for i in range(n):
        i_min = i
        for j in range(i + 1, n):
            if a[j] < a[i_min]:
                i_min = j
        a[i], a[i_min] = a[i_min], a[i]
    return a
s = 0
for i in a:
    if i > 0:
        list1 = [i] + list1
        s += 1
    elif i < 0:
        list2 = list2 + [i]
list_um = selection_sort(list1) + selection_sort(list2)
print(list_um, s)
