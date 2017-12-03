def knapsack(items, weight):
    """
    :param items: [(value, weight), ...]
    :param weight: int
    :return:  total_value, result_items
    """
    di = dict()
    keys = list()
    for item in items:
        v = item[0]
        w = item[1]
        for i in keys:
            if i + w > weight:
                continue
            else:
                if i + w not in di:
                    di[i + w] = (v + di[i][0], i)
                    keys.append(i + w)
                elif di[i + w][0] < v + di[i][0]:
                    di[i + w] = (v + di[i][0], i)
                    keys.append(i + w)
        keys.append(w)
        di[w] = (v, -1)

    print(di)


knapsack([(7, 5), (8, 4), (1, 6)], 12)
