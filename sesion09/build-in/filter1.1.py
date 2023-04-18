#map filter and reduce

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


def map_filter_reduce(numeros): 

    #map
    numeros_map = list(map(lambda x: x * 2, numeros))
    
    #filter
    numeros_filter = list(filter(lambda x: x % 2 == 0, numeros))
    
    #reduce
    numeros_reduce = reduce(lambda x, y: x + y, numeros_filter)
    
    return numeros_map, numeros_filter, numeros_reduce


numeros_map, numeros_filter, numeros_reduce = map_filter_reduce(numeros)

print(numeros_map)


print(numeros_filter)


print(numeros_reduce)


