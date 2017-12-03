def knapsack(items, weight):
    """
    :param items: [(value, weight), ...]
    :param weight: int
    :return:  total_value, result_items
    """
    li = [(0, -1) for _ in range(weight + 1)]
    for item in items:
        v = item[0]
        w = item[1]
        for i in range(weight, 0, -1):
            if li[i][0] == 0:
                continue
            elif i + w > weight:
                continue
            else:
                if li[i + w][0] < v + li[i][0]:
                    li[i + w] = (v + li[i][0], i)
                    break
        li[w] = (v, -1)

    return li


print(knapsack([(7, 5), (8, 4), (1, 6)], 12))
