# LeetCode Sept Challenge 25


class Compare:                                   # Using magic methods
    def __init__(self, num):
        self.value = str(num)
    def __lt__(self, other):                                           # called on comparison using '>'
        return (self.value + other.value) > (other.value + self.value)
    def __gt__(self, other):                                           # called on comparison using '<'
        return (self.value + other.value) < (other.value + self.value)
    def __eq__(self, other):                                           # called on comparison using '=='
        return (self.value + other.value) == (other.value + self.value)


def largestNumber(nums) -> str:
    numstr = [Compare(num) for num in nums]                 # arranging list in required sequence
    # print(numstr)
    numstr.sort()
    res = ''.join(elem.value for elem in numstr)            # get the result string by the values of 'Compare' class objects
    return res.lstrip('0') or 0                             # return res striping leading '0', if empty res return 0


print(largestNumber([3,30,34,5,9]))
print(largestNumber([1]))
print(largestNumber([10,2]))