#Challenge 1: Reverse String
#Input: cat
#Output: tac

def reverse(word):
    new_word = ""
    for i in word:
        new_word = i + new_word
    print("This is reverse func: {}".format(new_word))

#reverse("cat")

#Challenge 2: Sum the 2D Array

#   0  1  2  3  4
# [ 1, 2, 3, 4, 5] 0
# [ 6, 7, 8, 9,10] 1
# [11,12,13,14,15] 2
#Output: 120

from array import *
def sumArray(array):
    total = 0
    for x in array:
        print("I am in array {}".format(x))
        for y in x:
            print("I am looking at item {} in {}".format(y, x))
            total += y
    print("TOTAL {}".format(total))

#sumArray([[ 1, 2, 3, 4, 5], [ 6, 7, 8, 9,10], [11,12,13,14,15]])

#Challenge 3: Find the two numbers that equal the sum
# [1,3,4,6,11,23]
# Sum is 9
#Output: 3, 6 or 6, 3

from array import *
def twoSum(array, sum):
    #print("This is at least working. My array {} and my sum {}".format(array, sum))

    first = list(enumerate(array, 0))
    second = list(enumerate(array, 0))

    for i in first:
        #print("first: Tuple {}, Position {}, Value {}".format(i, i[0], i[1]))
        for j in second:
            #print("second: Tuple {}, Position {}, Value {}".format(j, j[0], j[1]))
            if i == j:
                #print("This is the same position: {}. Continuing...\n".format(i[0]))
                continue
            else:
                if i[1] + j[1] == sum:
                    #print("We found it!")
                    return i[1], j[1]

    #Return 0 if no summation could be found.
    return 0

#             0 1 2 3  4  5
print(twoSum([1,3,4,6,11,23], 9))   #>>> (3, 6)
print(twoSum([1,3,4,6,11,23], 1))   #>>> 0
print(twoSum([1,3,4,6,11,23], 34))  #>>> (11, 23)

