from math import log, trunc
a = int(input())

minus = 0
if (a < 0):
    a = abs(a)
    a = 2**(trunc(log(a, 2)) + 1) -1 - a
    a = a + 1
    minus += 1
cnt = minus

while (a > 0):
    if (a % 2): 
        cnt += 1
    a = a // 2
print(cnt)
