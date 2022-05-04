# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/2/2022
# Description: Finds the median of a list of numbers.

def find_median(some_nums):

    sorted_nums = sorted(some_nums)

    count = int(len(sorted_nums))

    median = 0

    if count%2 == 1:
        median = sorted_nums[count//2]

    else:
        middle = sorted_nums[count//2-1:count//2+1]
        median = (middle[0] + middle[1])/2

    return median