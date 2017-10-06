def count_inversions(data, x):
    arr_to_compare = data[x]

    inversions = []
    for i in range(len(data)):
        inversions += [[0, 0]]

    for i in range(len(data)):
        if i == x:
            inversions[i][0] = i
            continue

        data[i] = revert_array(arr_to_compare, data[i])
        inversions[i][0] = i
        inversions[i][1] = count_inversions_in_single_array(data[i])

    inversions.remove([x,0])
    inversions.sort(key = lambda a: a[1])



    return inversions



def revert_array(arr_to_compare, arr_to_revert):
    arr_to_compare = [x - 1 for x in arr_to_compare]
    new_arr = [0] * len(arr_to_revert)

    j = 0
    for i in arr_to_compare:
        new_arr[i] = arr_to_revert[j]
        j += 1

    return new_arr



def count_inversions_in_single_array(input):
    n = 0
    for i in range(len(input)):
        j = i

        while j != 0 and (input[j] < input[j - 1]):
            input[j], input[j-1] =  input[j-1], input[j]
            n += 1
            j -= 1

    return n
    

print(count_inversions([[3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
                        [3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
                        [3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
                        [3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
                        [3, 2, 10, 6, 9, 1, 5, 7, 4, 8],
                        [3, 2, 10, 6, 9, 1, 5, 7, 4, 8]], 1))
