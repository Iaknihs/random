"""

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""


def solution(arr1):
    """
    My first try already didn't use division, but if you Wanted to use division... just remove the if line and put a
    calc /= arr1[i] after the inner for loop.

    :param arr1: the array of numbers to work with
    :return:
    """
    res = []
    for i in range(len(arr1)):
        calc = 1
        for j in range(len(arr1)):
            if i != j:
                calc *= arr1[j]
        res.append(calc)
    return res


if __name__ == '__main__':
    print(solution([3, 2, 1]))
