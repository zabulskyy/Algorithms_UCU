class Median:
    def __init__(self):
        self.low_heap = []
        self.high_heap = []

    def high_heapify(self, i, A):
        length = len(A) - 1
        l = 2 * i + 1
        r = 2 * i + 2

        if l <= length and A[l] > A[i]:
            max_index = l

        else:
            max_index = i

        if r <= length and A[r] > A[max_index]:
            max_index = r

        if max_index != i:
            A[i], A[max_index] = A[max_index], A[i]
            self.high_heapify(max_index, A)

    def build_high_heap(self, A):
        for i in range(len(A) // 2, -1, -1):
            self.high_heapify(i, A)

    def low_heapify(self, i, A):
        length = len(A) - 1
        l = 2 * i + 1
        r = 2 * i + 2

        if l <= length and A[l] < A[i]:
            min_index = l

        else:
            min_index = i

        if r <= length and A[r] < A[min_index]:
            min_index = r

        if min_index != i:
            A[i], A[min_index] = A[min_index], A[i]
            self.low_heapify(min_index, A)

    def build_low_heap(self, A):
        for i in range(len(A) // 2, -1, -1):
            self.low_heapify(i, A)

    def add_element(self, value):
        if not self.low_heap and not self.high_heap:
            self.low_heap.append(value)

        elif value < max(self.low_heap):
            self.low_heap.append(value)
        else:
            self.high_heap.append(value)

        if len(self.low_heap) > len(self.high_heap) + 1:
            max_from_low = max(self.low_heap)
            self.high_heap.append(max_from_low)
            self.low_heap.remove(max_from_low)

        elif len(self.high_heap) > len(self.low_heap) + 1:
            min_from_high = min(self.high_heap)
            self.low_heap.append(min_from_high)
            self.high_heap.remove(min_from_high)

        self.build_low_heap(self.low_heap)
        self.build_high_heap(self.high_heap)

    def get_median(self):
        len_low = len(self.low_heap)
        len_high = len(self.high_heap)
        if (len_low + len_high) % 2:
            return max(self.low_heap) if len_low > len_high else min(self.high_heap)
        return max(self.low_heap), min(self.high_heap)

    def get_maxheap_elements(self):
        return self.high_heap

    def get_minheap_elements(self):
        return self.low_heap


m = Median()
for x in range(100, 0, -1):
    m.add_element(x)
    print(m.get_minheap_elements())

