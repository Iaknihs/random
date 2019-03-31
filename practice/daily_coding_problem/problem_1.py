"""

Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

"""


def solution(arr, k):
    """
    I think that counts as a 1-pass solution? dicts have a lookup time of O(1) for any reasonable inputs, due to being
    hashed.

    :param arr: array of numbers
    :param k: the number to add up to
    :return:
    """

    a = dict()
    for i in range(len(arr)):
        a[arr[i]] = i
        if k-arr[i] in a:
            print("yey")
            return
    print("nay")


if __name__ == '__main__':
    solution([1, 4, 5, 8, 32], 36)
    solution([1, 4, 5, 8, 32], 38)
