def flatten(a, depth = None): 
    flag = False 
    res = []
    l = a 
    cnt = 0
    while (not flag) and ((depth) and (cnt <= depth)): 
        flag = True
        for x in l:
            if isinstance(x, list):
                for y in x:
                    res.append(y)
                flag = False 
                cnt += 1
            else:
                res.append(x)
        l = res
        res = []
    return l
print(flatten([1, 2, [4, 5], [6, [7]], 8], depth = 11))