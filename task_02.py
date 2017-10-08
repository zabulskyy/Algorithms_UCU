def count_inversions(data, x):
    arr_to_compare = data[x]    # we will compare (sort by key of x) this array to others

    inversions = []
    for i in range(len(data)):
        # inversions will be written here
        inversions += [[0, 0]]

    for i in range(len(data)):
        if i == x:
            inversions[i][0] = i
            continue

        data[i] = revert_array(arr_to_compare, data[i])
        inversions[i][0] = i
        inversions[i][1] = count_inversions_in_single_array(data[i])

    inversions.remove([x,0])  # remove inverses of x with itself
    inversions.sort(key = lambda a: a[1])  # sort by 2nd parameter

    return inversions


def merge_sort(input):
    """
    actual merge sort
    """
    if len(input) == 2:
        return input if input[0] < input[1] else input[::-1]
    if len(input) == 1:
        return input

    l = len(input) // 2
    return merge_dac(sort_dac(input[:l]), sort_dac(input[l:]))


def merge(input1, input2):
    """
    merge two sorted arrays into one sorted array
    """
    input = []
    for i in range(len(input1) + len(input2)):
        if not input1:
            input += input2
            return input
        if not input2:
            input += input1
            return input
        if input1[0] < input2[0]:
            input.append(input1[0])
            input1 = input1[1:]
        else:
            input.append(input2[0])
            input2 = input2[1:]
    return input


def revert_array(arr_to_compare, arr_to_revert):
    """
    sort arr_to_revert by key of arr_to_compare, for example:
    arr_to_compare = [1, 0, 2]
    arr_to_revert = [1, 2, 3]
    return : [2, 1, 3]
    """
    arr_to_compare = [x - 1 for x in arr_to_compare]
    new_arr = [0] * len(arr_to_revert)

    j = 0
    for i in arr_to_compare:
        new_arr[i] = arr_to_revert[j]
        j += 1

    return new_arr



def count_inversions_in_single_array(input):
    """
    we do actual 'sorting' and counting how many steps do we need to sort
    this array, thus we get number of inversions
    """
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
