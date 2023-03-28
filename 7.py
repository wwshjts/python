def flatten(a, depth = None): 
    flag = False 
    res = []
    l = a 
    cnt = 0
    while (not flag) and ((depth) and (cnt < depth)): 
        flag = True
        for x in l:
            if isinstance(x, list):
                for y in x:
                    res.append(y)
                flag = False 
            else:
                res.append(x)
        cnt +=1
        l = res
        res = []
    return l
print(flatten([1, 2, [4, 5], [6, [7, [34]]], 8, [2,[1, [43,21]]]], depth = 2))