"""
Given a list of integers `lst`, any integer with a frequency that is equal to its value is considered a **lucky integer**.

Write a function that returns the lucky integer from the array. If the array contains multiple lucky integers, return the largest one. If there are no lucky integers return -1.

**Example 1**:

Input: arr = [2,3,3,3,4]
Output: 3

**Example 2**:

Input: arr = [1,2,2,3,3,3,4,4,4,4]
Output: 4

**Example 3**:

Input: arr = [1,1,2,2,2]
Output: -1
"""
def find_lucky(lst):
    # Your code here
    occurrences = {}
​
    # count number of occurrences for each num in list 
    for n in lst:
        if n in occurrences:
            occurrences[n] += 1
        else:
            occurrences[n] = 1
​
    # add all nums that are possible lucky numbers to a candidates list 
    candidates = [key for key, val in occurrences.items() if key == val]
​
    # return the largest candidate or -1 if there is no lucky number 
    if len(candidates) == 0:
        return -1
​
    return max(candidates)