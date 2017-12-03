def knapsack(items, weight):
    """
    :param items: [(value, weight), ...]
    :param weight: int
    :return:  total_value, result_items
    """

    # initialize local variables
    di = dict()
    keys = set()  # keys of di, must be assigned as dict cannot be dynamically changed during iteration
    k = set()

    # iterate items
    for item in range(len(items)):
        v = items[item][0]  # value of current item
        w = items[item][1]  # weight of current item

        # iterating current keys
        for i in keys:
            k = set()
            # if we can't put i element and item element together
            if i + w > weight:
                continue

            # if i + w is currently zero
            if i + w not in di:
                di[i + w] = (v + di[i][0], i, item)
                k.add(i + w)

            # if i + w is less than current v + di[i]
            elif di[i + w][0] < v + di[i][0]:
                di[i + w] = (v + di[i][0], i, item)
                k.add(i + w)

        # update keys
        keys.add(w)
        keys = keys.union(k)

        # add current item to itself's cell
        di[w] = (v, -1, item)

    print(di)

    # finding max value and its path
    current = di[max(di, key=lambda a: di[a][0])]
    total_value = current[0]
    path = list()
    while 1:
        path.append(current[2])
        i = current[1]
        if i == -1:
            break
        current = di[i]
    return total_value, path


print(knapsack([(7, 5), (8, 4), (1, 6)], 12))
