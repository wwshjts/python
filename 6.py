def flatten(a): 
    flag = False 
    res = []
    l = a 
    while (not flag): 
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
print(flatten([1, 2, [4, 5], [6, [7]], 8]))