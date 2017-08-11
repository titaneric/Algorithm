import random
import math


def insertion_sort(array: list):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i > -1 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

    return array


def __merge(array, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [array[p + i - 1] for i in range(1, n1 + 1)]
    R = [array[q + j] for j in range(1, n2 + 1)]

    L.append(math.inf)
    R.append(math.inf)

    i, j = (0, 0)
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1


def __merge_sort(array, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        __merge_sort(array, p, q)
        __merge_sort(array, q + 1, r)
        __merge(array, p, q, r)


def merge_sort(array):
    __merge_sort(array, 0, len(array) - 1)
    return array


def __find_max_crossing_subarray(array, low, mid, high):
    left_sum = -math.inf
    summation = 0
    for i in reversed(range(low, mid + 1)):
        summation += array[i]
        if summation > left_sum:
            left_sum = summation
            max_left = i

    right_sum = -math.inf
    summation = 0
    for i in range(mid + 1, high + 1):
        summation += array[i]
        if summation > right_sum:
            right_sum = summation
            max_right = i
    return max_left, max_right, left_sum + right_sum


def __find_maximum_subarray(array, low, high):
    if high == low:
        return low, high, array[low]
    else:
        mid = math.floor((low + high) / 2)
        left_low, left_high, left_sum = __find_maximum_subarray(
            array, low, mid)
        right_low, right_high, right_sum = __find_maximum_subarray(
            array, mid + 1, high)
        cross_low, cross_high, cross_sum = __find_max_crossing_subarray(
            array, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(array):
    return __find_maximum_subarray(array, 0, len(array) - 1)


def quick_sort(array, rand=True):
    __quick_sort(array, 0, len(array) - 1, rand) 
    return array


def __quick_sort(array, p, r, rand):
    if p < r:
        q = __randomized_partition(array, p, r) if rand else __partition(array, p, r)
        __quick_sort(array, p, q - 1, rand)
        __quick_sort(array, q + 1, r, rand)


def __randomized_partition(array, p, r):
    i = random.randint(p, r)
    array[r], array[i] = array[i], array[r]
    return __partition(array, p, r)


def __partition(array, p, r, partition_index=None):
    if partition_index is not None:
        array[r], array[partition_index] = array[partition_index], array[r]

    x = array[r]

    i = p - 1
    for j in range(p, r):
        if array[j] < x:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def counting_sort(array, k):
    sorted_list = [0 for _ in range(len(array))]
    tmp_list = [0 for _ in range(k+1)]
    
    for j in range(len(array)):
        tmp_list[array[j]] += 1
    
    for i in range(1, k+1):
        tmp_list[i] += tmp_list[i-1]

    for j in reversed(range(len(array))):
        sorted_list[tmp_list[array[j]] - 1] = array[j]
        tmp_list[array[j]] -= 1

    return sorted_list


def radix_sort(array, d):
    return 


def max_and_min(array):
    if len(array) % 2 == 0:
        if array[0] >= array[1]:
            current_maximum, current_minimum = (array[0], array[1])
        else:
            current_maximum, current_minimum = (array[1], array[0])
    else:
        current_maximum = array[0]
        current_minimum = array[0]

    for i, j in zip(array[::2], array[1::2]):
        if i >= j:
            current_maximum = i if i > current_maximum else current_maximum
            current_minimum = j if j < current_minimum else current_minimum
        else:
            current_maximum = j if j > current_maximum else current_maximum
            current_minimum = i if i < current_minimum else current_minimum

    return current_maximum, current_minimum


def __randomized_select(array, p, r, i):
    if p == r:
        return array[p]
    q = __randomized_partition(array, p, r)
    k = q - p + 1
    if i == k:
        return array[q]
    elif i < k:
        return __randomized_select(array, p, q - 1, i)
    else:
        return __randomized_select(array, q + 1, r, i - k)


def randomized_select(array, i):
    return __randomized_select(array, 0, len(array) - 1, i)


# Incorrect
def select(array, i):
    if len(array) == 1:
        return array[0]
    else:
        medians = []
        for subarray in group_array(array, 5):
            sorted_subarray = insertion_sort(subarray)
            median_index = math.floor((len(subarray) + 1)//2)
            median_index -= 1
            medians.append(sorted_subarray[median_index])
        
        median_index = math.floor((len(medians) + 1)//2)
        median_of_medians = select(medians, median_index)
        k = __partition(array, 0, len(array) - 1, partition_index=array.index(median_of_medians))
   
        if (k + 1) == i:
            return array[k]
        elif i < (k + 1):
            return select(array[:k], i)
        else:
            return select(array[k + 1:], i - k - 1)


def group_array(array, group_size):
    return [array[i: i + group_size] for i in range(0, len(array), group_size)]


if __name__ == "__main__":
    
    
    for _ in range(100000):
        random_list = [random.randint(-100, 100) for _ in range(100)]        
        index = random.randint(1, 100)
        sorted_list = sorted(random_list)
        assert randomized_select(random_list, index) == sorted_list[index - 1]
        assert select(random_list, index), sorted_list[index - 1]
        assert quick_sort(random_list) == sorted(random_list)
        assert insertion_sort(random_list) == sorted(random_list)
        assert merge_sort(random_list) == sorted(random_list)
        assert max_and_min(random_list) == (max(random_list), min(random_list))
        # assert randomized_select(random_list, index) == sorted(random_list)[index]
    # A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    # print(find_max_crossing_subarray(A))
    # A = [-1, 16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
    # max_heapify(A, 2)
    # print(A)
    # A = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    # heap = build_max_heap(A)
    # print(heap)
    # A = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    # print(heap_sort(A))
    A = [2, 5, 3, 0, 2, 3, 0, 3]
    assert counting_sort(A, max(A)) == sorted(A)
