"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #12 - One Up! (addone.py)


Author: Paul Thai

Difficulty Level: 6/10

Background: Do you know how to add? Good! I have just the question for you!
Most people know how to add by one, but can you add by one in this problem???

Prompt: Given an array, add one to the ones column!

Constraints: You cannot map/join the list into a single number, add one, and then turn it back into a list.
That's cheating (because I have done it before...) so you must modify the list itself. Be careful of place values!

Test Cases:
a = [1, 2, 3]; output = [1, 2, 4]
a = [9]; output = [1,0]
a = [1, 4, 6, 0]; output = [1]
"""


class Solution:
    def addOne(self, ary):
        # type ary: list
        # return type: list

        # TODO: Write code below to return a list "ary" with the solution to the prompt
        back_ary = reversed(ary)
        back_ary[0] = back_ary[0] + 1
        for i in range(0, len(ary) -1):
            if back_ary[i] > 9:
                back_ary[i] = 0
                back_ary[i+1] += back_ary[i] - 9
        return reversed(back_ary)


def main():
    array = input().split(" ")
    for x in range(0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.addOne(array)
    print(ans)


if __name__ == "__main__":
    main()