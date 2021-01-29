# Solutions to @svpino 's code challenge on twitter
# The original thread can be found on https://twitter.com/svpino/status/1354048200601198593

from random import shuffle
a = list(range(1, 21))
shuffle(a)
# 1 - Reverse an array in place
def reverse_inplace(array):
    len_arr = len(array)
    for i in range(int(len_arr / 2)):
        index = len_arr - i - 1
        temp = array[i]
        array[i] = array[index]
        array[index] = temp

    return array


# 2 - Find missing number (only one number is missing out of 100) in an unsorted array that contains numbers from 1-100
def missing(array):
    max_sum = 5050
    for i in array:
        max_sum -= i
    return max_sum


# 3 - Find the duplicate number (only one is duplicate) in an unsorted array that contains numbers from 1-100
def duplicate(array):
    return missing(array) * -1


# 4 - Remove duplicates in an unsorted array
def remove_duplicate(array):
    d = {}
    for i in array:
    	if i not in d:
    		d[i] = 1
    return list(d.keys())


# 5 - Find largest and smallest number in unsorted array
def minmax(array):
    minimum = array[0]
    maximum = array[0]
    for item in array[1:]:
        if item > maximum:
            maximum = item
        elif item < minimum:
            minimum = item
    return minimum, maximum


# 6 - Function that finds a subarray whose sum is equal to a given value
def summed_subarray(array, total):
    sigma = 0
    start = 0
    end = 0
    for i in range(len(array)):
        if sigma < total:
            sigma += array[i]
            end += 1
        elif sigma > total:
            sigma -= array[start]
            start += 1
        elif sigma == total:
            return array[start: end]
    return []



# 7 - Function that finds the contiguous subarray of a given size with the largest sum
def largest_sum_subarray(array, size):
    total = sum(array[:size])
    maximum = total
    start = 0
    end = size
    for i in range(0, len(array) - size):
        total = total + array[i + size] - array[i]
        if total > maximum:
            maximum = total
            start = i + 1
            end = i + size + 1
    return array[start: end]


# 8 - Function that, given two arrays, finds the longest common subarray present in both of them
# I could not figure this out
def longest_common_subarray(array1, array2):

    longer = max(array1, array2, key=len)
    shorter = min(array2, array1, key=len)
    '''a lot to do'''
    longest = []
    len_longest = 0
    for size in range(1, len(shorter)):
        pass


# 9 - Function that, given two arrays, finds the length of the shortest array that contains both input arrays as subarrays
def array_lcm(array1, array2):
    longer = max(array1, array2, key=len)  # DO NOT CHANGE THE ORDER
    shorter = min(array2, array1, key=len)  # DO NOT CHANGE THE ORDER
    len_long = len(longer)
    len_short = len(shorter)

    ### Uncommenting the print statements visualises how the algorithm proceeds

    for i in range(1, len_short + 1):
        # print(longer[-i:], shorter[:i])
        if longer[-i:] == shorter[:i]:
            return len_long + len(shorter[i:])

    # This just checks if the shorter array is inside the longer array

    for j in range(1, len_long + 1 - i):
        # print(longer[-j + i - 1:-j + 2 * i - 1], shorter)
        if longer[-j + i - 1:-j + 2 * i - 1] == shorter:
            return len_long

    for i in range(len_short - 1, 0, -1):
        # print(shorter[-i:], longer[:i])
        if shorter[-i:] == longer[:i]:
            return len_short + len(longer[i:])

    return len_long + len_short


# 10 - Function that, given an array, determines if you can partition it in two separate subarrays such that the sum of elements in both subarrays is the same
def equal_sum_array(array):
    total1 = 0
    total2 = sum(array)
    for i in range(len(array)):
        total1 += array[i]
        total2 -= array[i]
        if total1 == total2:
            return array[:i + 1], array[i + 1:]
        elif total1 > total2:
            return None


# 11 - Function that, given an array, divides it into two subarrays, such as the absolute difference between their sums is minimum
def min_diff_array(array):
    total1 = 0
    total2 = sum(array)
    minimum = abs(total1 - total2)
    index = 0
    for i in range(len(array)):
        total1 += array[i]
        total2 -= array[i]
        abs_diff = abs(total1 - total2)
        if abs_diff < minimum:
            minimum = abs_diff
            index = i
    return array[:index+1], array[index+1:]
