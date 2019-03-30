"""
[2019-02-11] Challenge #375 [Easy] Print a new number by adding one to each of its digit
Description
A number is input in computer then a new no should get printed by adding one to each of its digit.
If you encounter a 9, insert a 10 (don't carry over, just shift things around).

For example, 998 becomes 10109.

Bonus
This challenge is trivial to do if you map it to a string to iterate over the input, operate, and then cast it back.
Instead, try doing it without casting it as a string at any point, keep it numeric (int, float if you need it) only.

Credit
This challenge was suggested by user /u/chetvishal, many thanks!
If you have a challenge idea please share it in /r/dailyprogrammer_ideas and there's a good chance we'll use it.
"""


def simple_solution(num):
    """
    Trivial solution using string conversion.

    :param num: the number to process
    :return:
    """
    text = str(num)
    res = ''
    # loop increases each chars int value by 1 and stores it back into a string.
    for char in text:
        res += str(int(char)+1)
    print(res)


def bonus_solution(num):
    """
    Bonus challenge solution not allowing string conversion.

    :param num: the number to process
    :return:
    """
    digit_array = list()
    # loop separates all digits and stores them as array elements
    while num:
        digit = num % 10
        digit_array.append(digit)
        num //= 10

    # loop increases newnum to make space for other digits each iteration and then adds increased digit
    newnum = 0
    for digit in reversed(digit_array):
        if digit > 0:
            newnum *= 10
            if digit > 8:
                newnum *= 10
        newnum += digit + 1
    print(newnum)


if __name__ == '__main__':
    simple_solution(39)
    bonus_solution(39)
    bonus_solution(38)

