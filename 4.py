d = {(2,1) : 231,  "Petrov" : 431, "Sidorov" : 231, "Kozlov" : 231, "Ivanov" : '2'}

keys = d.keys()
items = d.items()
new_d = {}

for key in keys:
    if d[key] not in new_d:
        new_d[d[key]] = key
    else:
        if not isinstance(new_d[d[key]], list):
            new_d[d[key]] = [new_d[d[key]]]
        new_d[d[key]].append(key)
for key in new_d:
    if isinstance(new_d[key], list):
        new_d[key] = tuple(new_d[key])

print(new_d)
