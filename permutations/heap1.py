def heap_permutations(data, k):
    if k == 1:
        print(data)
        return

    for i in range(k):
        heap_permutations(data, k-1)
        if k % 2 == 0:
            data[i], data[k-1] = data[k-1], data[i]
        else:
            data[0], data[k-1] = data[k-1], data[0]


elements = [1, 2, 3, 4, 5]
heap_permutations(elements, len(elements))
