class Sorting:
    def bubble_sort(alist):
        length = len(alist)
        for i in range(length - 1):
            # i means how many rounds to compare
            for j in range(length - i - 1):
                # j represents the range of elements in each round of comparison, because each round of comparison will sort the position of an element,
                # So in the next round of comparison, there will be one less element, so I will be subtracted
                if alist[j] > alist[j + 1]:
                    alist[j], alist[j + 1] = alist[j + 1], alist[j]

    def selection_sort(alist):
        length = len(alist)
        for i in range(length - 1, 0, -1):
            for j in range(i):
                if alist[j] > alist[i]:
                    alist[j], alist[i] = alist[i], alist[j]

    def insert_sort(alist):
    for i in range(1, len(alist)):
        # Starting with the second element, take out one element at a time and insert the previous sequence to make it ordered
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]

    def shell_sort(alist):
        n = len(alist)
        # Initial step size
        gap = n / 2
        while gap > 0:
            # Insert sort by step
            for i in range(gap, n):
                j = i
                # Insert sort
                while j >= gap and alist[j - gap] > alist[j]:
                    alist[j - gap], alist[j] = alist[j], alist[j - gap]
                    j -= gap
            # The new step size is obtained
            gap = gap / 2

