array = [
    [1, 5, 6, 8], 
    [2, 4, 10, 12], 
    [3, 7, 9, 11], 
    [13, 14, 15, 16]
]

array_length = len(array)

def appender(record,
             agg):    
    for i in record: 
        agg.append(i)
    return agg
    
agg = []
for i in range(array_length):
    agg = appender(array[i], agg)
agg.sort()
    
print(agg)
