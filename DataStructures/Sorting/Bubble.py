a = [3,4,1,5,6,7]

n = len(a)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if a[j] > a [j + 1]:
            a[j], a[j + 1] = a[j + 1],a[j]
            swapped = True
    if not swapped:
        break

print(a)