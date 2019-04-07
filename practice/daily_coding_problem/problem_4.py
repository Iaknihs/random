"""

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""
import random  # for testing


def swap(arr, i, j):
    """
    Help function to swap array elements at indices i and j
    space = time = O(1)

    :param arr: the array to swap in
    :param i: index to swap with j
    :param j: index to swap with i
    :return:
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def solution(arr):
    """
    Boy, I actually had to look up a hint for this one. Wrote the actual code myself, but I didn't notice that numbers
    that are larger than what fits into the array.. don't matter... since they can only exist if something is missing
    beforehand. Well darn. Interesting task, however.

    :param arr: array to process
    :return:
    """
    print(arr)
    last_relevant_index = len(arr)-1
    i = 0
    # LOOP: time: O(len(arr)), since each iteration either i increases by 1, or last_rel... decreases by 1.
    #       space: O(1), since only variables of constant size are used (except for the given array)
    # Move non-positive integers to the right and remember which is the last relevant (positive) element
    while i <= last_relevant_index:
        if arr[i] <= 0:
            swap(arr, i, last_relevant_index)
            last_relevant_index -= 1
        else:
            i += 1
    print(arr)
    # LOOP: time: O(len(arr)), space: O(1) except for the array, which is edited by swapping signs.
    #
    for i in range(0, last_relevant_index+1):
        # -1, because we start counting at 1 instead of 0 in the task.
        idx = abs(arr[i])-1
        if 0 <= idx <= last_relevant_index:
            arr[idx] = -arr[idx]
    print(arr)
    # LOOP: time: O(len(arr)), space: O(1)
    for i in range(0, last_relevant_index+1):
        if arr[i] > 0:
            # +1, because we start counting at 1 instead of 0 in this task.
            print(i+1)
            return
    # +1, because we start counting at 1 instead of 0 in the task (urgh), +1 because we want the next element post-end
    print(last_relevant_index+2)


if __name__ == '__main__':
    solution([3, 4, -1, 1])
    solution([1, 2, 0])
    solution([1, 2, -1])
    # wrote another test thingy which randomises to help with finding potential bugs!
    solution(random.sample(range(-10, 10), 15))
    solution(random.sample(range(-15, 15), 15))
    solution(random.sample(range(-8, 8), 15))
    solution(random.sample(range(-15, 15), 15))
    solution(random.sample(range(-15, 15), 15))

