from flatten import flatten #flatten from 7.py
def format_table(benchmarks, algos, results):
    algos = ['Benchmark'] + algos 
    results = [list(map(str,x)) for x in results]
    max_col_len = len((max(benchmarks + algos + flatten(results, 2), key = len))) + 2
    for word in algos:
        print(f"|{word.center(max_col_len)}", end = '')
    print('|')
    for i in range(len(benchmarks)):
        bench = benchmarks[i]
        print('|' + bench.center(max_col_len), end = '|')
        for j in range(len(results[i])):
            spaces = (max_col_len - len(algos[j+1]))
            spaces = spaces//2 + spaces % 2 
            print(' ' * spaces + results[i][j] + ' '*(max_col_len - spaces - len(results[i][j])),end = '|')
            
        print()
            
        
     
    
format_table(["best case", "worst case"],
["quick sort", "merge sort", "bubble sort", "bogo"],
[[1.2311, 1.2356, 2.0, 5.2113213], [3.3, 2.9, 3.91234238743, 41.1]])