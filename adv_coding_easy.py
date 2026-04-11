# Suppose an array of integers is given as the input to a program.
# NOTE: The integers can be (-)ve, 0 or (+)ve.
# Find subset of the array (solution subset can be of length 1 or the entire array length itself)
# such that the product of all the elements is the maximum product obtained 
# when compared to the product obtained by all the possible subsets of the array.
# INPUT: array [1<=len(array)<2^40] -- e.g (input): -1 2 3 4 -- read as `str` dtype not `int` dtype
# OUTPUT: the maximum product obtained from all possible subsets of the input array elements

# --> Certain modules and functions are used in the code, which are explained at the end of the code snippet for better understanding.


from itertools import combinations # description at the end of code snippet | search $1

# Fuction `all_sublists` to generate all possible sublists of a given list
def all_sublists(lst):
    n = len(lst)
    for r in range(2, n + 1):  # r = size of sublist
        for combo in combinations(lst, r):
            if 0 in combo:
                continue  # Skip sublists that contain zero
            yield list(combo)

# Main program

# Input and processing
input_array =list(map(int, input().split()))  # e.g. input: "1 2 3"

# Calculate the maximum of the input array --- to handle the case when all elements are negative or zero
max_product=max(input_array)

if len(input_array) == 1:
    print(max_product)  # If only one element, return that element as the max product
elif len(input_array) == 2:
    print(max(max_product, input_array[0] * input_array[1]))  # If two elements, return the maximum of the individual elements and their product
elif all(x <= 0 for x in input_array): # ---------> all() description is at end of code snippet | search $2
    # If all elements are non-positive, return the maximum element (which could be zero or the least negative)
    print(max_product)
else:
    for sub in all_sublists(input_array):
        product = 1
        for x in sub:
            product *= x
        max_product = max(max_product, product)
    print(max_product)



# -------------------------------------------------------------------------------------------------------------

# $1 <---
# itertools.combinations() --- part of itertools module in Python, 
#                          --- provides various functions that work on iterators to produce complex iterators.
# The itertools.combinations() function generates all possible unique combinations of a specified length from an iterable, 
# where order does not matter and elements are treated as unique by their position.
# How it works:
# - itertools.combinations(iterable, r) returns an iterator producing r-length tuples from the input iterable.
# - The output is in lexicographic order(dictionary order) based on the input order.
# - If the iterable is sorted, the combinations will also be sorted.
# Example – From String:
# from itertools import combinations
# word = "WXY"
# for c in combinations(word, 2):
#    print(''.join(c))
# Output:
# WX
# WY
# Y

# $2 <---
# all()
# Built-in function, checks whether all elements in an iterable are truthy (evaluate to True).
# Syntax: all(iterable)
# - Returns True if all elements are truthy.
# - Returns False if any element is falsy (0, False, None, '', empty container, etc.).
# - Returns True for an empty iterable (vacuous truth).
#
# Example usage:
# All True values
# print(all([True, True, True]))       # True
# 
# Contains a False value
# print(all([True, False, True]))      # False
# 
# Numbers (0 is False)
# print(all([1, 2, 3]))                # True
# print(all([1, 0, 3]))                # False
# 
# Strings (empty string is False)
# print(all(["apple", "banana", "cherry"]))  # True
# print(all(["apple", "", "cherry"]))        # False
# 
# Empty iterable
# print(all([]))                        # True
# 
# Dictionary (checks keys)
# print(all({"a": 1, "b": 2}))          # True
# print(all({"a": 1, "b": 0}))          # False
