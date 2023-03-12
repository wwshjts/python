a = input().split(' ')
b = input().split(' ')
res = []
for i in range(min(len(a), len(b))):
    res.append((a[i], b[i]))

print(res)