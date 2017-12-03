def knapsack(items, weight):
    """
    :param items: [(value, weight), ...]
    :param weight: int
    :return:  total_value, result_items
    """

    # initialize local variables
    di = dict()  # {weight:(max value, where from, index in original list)}
    keys = set()  # keys of di, must be assigned as dict cannot be dynamically changed during iteration
    k = set()

    # iterate items
    for item in range(len(items)):
        v = items[item][0]  # value of current item
        w = items[item][1]  # weight of current item

        # iterating current keys
        keys = sorted(list(keys), reverse=True)
        for i in keys:
            # if we can't put i element and item element together
            if i + w > weight:
                continue
            # if i + w is currently zero
            if i + w not in di:
                di[i + w] = (v + di[i][0], i, list(di[i][2]) + [item])
                k.add(i + w)

            # if i + w is less than current v + di[i]
            elif di[i + w][0] < v + di[i][0]:
                di[i + w] = (v + di[i][0], i, list(di[i][2]) + [item])
                k.add(i + w)

        # update keys
        keys = set(keys).union(k)
        k = set()

        # add current item to itself's cell
        if w not in di:
            di[w] = (v, -1, [item])
            keys.add(w)
        elif di[w][0] < v:
            di[w] = (v, -1, [item])
            keys.add(w)
        print("val: {0}, wei: {1}".format(v, w))
        print(di)

    # finding max value and its path
    max_value = di[max(di, key=lambda a: di[a][0])]
    total_value = max_value[0]
    path = max_value[2]
    return total_value, path


print(knapsack([[7, 5], [8, 4], [9, 3], [10, 2], [1, 10], [3, 15], [8, 10], [6, 4], [5, 3], [7, 3]], 20))
