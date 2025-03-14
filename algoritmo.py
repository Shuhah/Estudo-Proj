def bucketSort(arr): #array
    # puxar o min e max
    minV = min(arr)
    maxV = max(arr)

    bucket_count = len(arr) # bucket n
    bucket_size = (maxV - minV) / bucket_count # tamanho do bucket

    buckets = [[] for _ in range(bucket_count)] 

    for n in arr:

        index = int((n - minV) / bucket_size)
        if index == bucket_count:
            index -= 1
        buckets[index].append(n)

    sorted_arr = []
    for baldão in buckets:
        sorted_arr.extend(sorted(baldão)) #ordenar os bvckets

    return sorted_arr

#prova
arr = [42, 23, 4.2, 55, 69, 125, 2.2, 2]
sorted_arr = bucketSort(arr)
print("tome", sorted_arr)

#O Bucket Sort é um algoritmo de ordenação que divide os elementos em vários grupos (ou "baldes") e, em seguida, ordena cada grupo individualmente, geralmente usando outro algoritmo de ordenação (como o Insertion Sort). Em seguida, ele concatena todos os baldes ordenados para produzir a lista final ordenada.