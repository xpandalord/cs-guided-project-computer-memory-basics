"""
In order to solve this challenge you will need to [review the rules of Roman
Numerals](https://www.mathsisfun.com/roman-numerals.html).

Given a Roman Numeral (as a string), convert it to an integer. Your input is
guaranteed to be a Roman Numeral value from 1 to 3999.

Example 1:

Input: "IV"
Output: 4

Example 2:

Input: "XII"
Output: 12

Example 3:

Input: "MCMLXXXIV"
Output: 1984
"""
def roman_to_integer(roman):
    # Your code here
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
​
    total = 0
    i = 0
​
    # we'll want to look at roman numerals two-at-a-time 
    while i < len(roman):
        # subtractive case 
        if i + 1 < len(roman) and mapping[roman[i]] < mapping[roman[i + 1]]:
            # if the left numeral < right numeral
            # subtract left from right 
            diff = mapping[roman[i + 1]] - mapping[roman[i]]
            # add the result to our total
            total += diff
            # we need to skip both numerals 
            i += 2
        # additive case
        else:
            # otherwise, left numeral >= right numeral 
            # add the left numeral to our total 
            total += mapping[roman[i]]
            i += 1
​
    return total 
​
print(roman_to_integer("MCMLXXXIV"))

