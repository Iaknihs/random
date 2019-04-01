import math

"""

[2019-03-13] Challenge #376 [Intermediate] The Revised Julian Calendar
Background
The Revised Julian Calendar is a calendar system very similar to the familiar Gregorian Calendar,
but slightly more accurate in terms of average year length.

The Revised Julian Calendar has a leap day on Feb 29th of leap years as follows:

Years that are evenly divisible by 4 are leap years.

Exception: Years that are evenly divisible by 100 are not leap years.

Exception to the exception: Years for which the remainder when divided by 900 is either 200 or 600 are leap years.

For instance, 2000 is an exception to the exception: the remainder when dividing 2000 by 900 is 200.
So 2000 is a leap year in the Revised Julian Calendar.

Challenge
Given two positive year numbers (with the second one greater than or equal to the first),
find out how many leap days (Feb 29ths) appear between Jan 1 of the first year,
and Jan 1 of the second year in the Revised Julian Calendar.
This is equivalent to asking how many leap years there are in the interval between the two years,
including the first but excluding the second.

leaps(2016, 2017) => 1
leaps(2019, 2020) => 0
leaps(1900, 1901) => 0
leaps(2000, 2001) => 1
leaps(2800, 2801) => 0
leaps(123456, 123456) => 0
leaps(1234, 5678) => 1077
leaps(123456, 7891011) => 1881475

For this challenge, you must handle very large years efficiently, much faster than checking each year in the range.

leaps(123456789101112, 1314151617181920) => 288412747246240

Optional bonus
Some day in the distant future,
the Gregorian Calendar and the Revised Julian Calendar will agree that the day is Feb 29th,
but they'll disagree about what year it is. Find the first such year (efficiently).

"""


def is_leap(year):
    """
    Years that are evenly divisible by 4 are leap years.

    Exception: Years that are evenly divisible by 100 are not leap years.

    Exception to the exception: Years for which the remainder when divided by 900 is either 200 or 600 are leap years.

    :param year: (check if a specific year is a leap year
    :return:
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 900 in [200, 600]:
                return 3
            return 2
        return 1
    return 0


def count_leaps_slow(start, end):
    """
    I wrote a slow, iterative version first to get a feeling for the math that's happening.
    It works, but isn't recommended on big scales.
    See compute_leaps_fast() for a faster version.

    :param start: start year (included)
    :param end: end year (excluded)
    :return:
    """
    count = 0
    year = start
    while year < end:
        leap = is_leap(year)
        if leap > 0:
            # skip 3 years as leap can only be every 4 years
            year += 3
            if leap in [1, 3]:
                count += 1
        year += 1
    return count


def compute_leaps_fast(start, end):
    """
    A O(1) version (where n would be number of years in the range, as the slow version is O(n)),
    quickly computing how many leap years are in a range.

    :param start: start year (included)
    :param end: end year (excluded)
    :return:
    """
    return compute_leaps_fast_from_0(end)-compute_leaps_fast_from_0(start)


def compute_leaps_fast_from_0(end):
    """
    utility function calculating the number of leap years between 0 and N in O(1)

    :param end: end year (excluded)
    :return:
    """
    end = end-1
    if end < 1100:
        raise ValueError("year number too small to apply all leap year rules.")
    leaps = math.floor(end/4) - math.floor(end/100) + math.floor((end-200)/900) + math.floor((end-600)/900)
    return leaps


def bonus_challenge():
    raise NotImplementedError("Details on the gregorian calendar weren't given in the task, \n"
                              "and I couldn't be bothered to look it up myself, so I didn't implement this yet. \n"
                              "I'll probably look it up some other time. If I remember.")


if __name__ == '__main__':
    print(compute_leaps_fast(2016, 2017))
    print(compute_leaps_fast(2019, 2020))
    print(compute_leaps_fast(1900, 1901))
    print(compute_leaps_fast(2000, 2001))
    print(compute_leaps_fast(2800, 2801))
    print(compute_leaps_fast(123456, 123456))
    print(compute_leaps_fast(1234, 5678))
    print(compute_leaps_fast(123456, 7891011))
    print(compute_leaps_fast(123456789101112, 1314151617181920))
    # bonus_challenge()
