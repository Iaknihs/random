"""

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

"""


def solution(arr):
    """
    This one seemed pretty straight-forward to me. Just go through the array and sum up the optimum for the sub array
    until i.

    :param arr:
    :return:
    """
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0
    arr[2] += arr[0]
    for i in range(3, len(arr)):
        arr[i] += max(arr[i-2], arr[i-3], -arr[i-1] if arr[i-1] < 0 else -1)
        if arr[i] == 0:
            arr[i] = -arr[i]

    return arr[-1]


def test():
    print(solution([2, 3, 5, 6, -1, -2, 0, 5, 3, 2, 3, 1]))
    print(solution([2, 4, 6, 2, 5]))
    print(solution([5, 1, 1, 5]))


if __name__ == '__main__':
    test()
