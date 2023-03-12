d = {'Ivanov' : 231,  "Petrov" : 431, "Sidorov" : 231, "Kozlov" : 231}

keys = d.keys()
new_d = {}

for key in keys:
    if d[key] not in new_d:
        new_d[d[key]] = key
    else:
        if type(new_d[d[key]]) == type(tuple()):
            print(new_d[d[key]])
            tmp = [x for x in new_d[d[key]]] 
            tmp.append(key)
            tmp = tuple(tmp)
            new_d[d[key]] = tmp
        else:
            new_d[d[key]] = (new_d[d[key]], key)
            print(new_d)

print(new_d)




