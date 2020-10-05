"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    # keep dict mapping upper-case chars to lower-case chars 
    # traverse the string char by char 
        # if we see an uppercase char 
        # convert it to its lower-cased version by checking if
        # the char exists in the dict 
​
    # Your code here
    # should lower-case all chars in the string 
    # chars that are already lower-cased should not be affected 
    # otherwise, capitalized chars should be lower-cased 
​
    # take our string and turn it into a list of chars 
    # because strings are immutable in Python 
    encoded_chars = [ord(char) for char in string]
​
    # print(encoded_chars)
​
    # if we see an uppercase char 
    for i in range(len(encoded_chars)):
        # to check if a char is uppercased, check if 
        if encoded_chars[i] >= 65 and encoded_chars[i] <= 90:
        # ord(char) >= 65 and ord(char) <= 90
        # add 32 to it to turn it into its lowercase version 
            encoded_chars[i] += 32
​
    # print(encoded_chars)
​
    decoded_chars = [chr(char) for char in encoded_chars]
​
    # print(decoded_chars)
​
    # return all of the decoded chars as a string instead of as a list 
    return "".join(decoded_chars)
​
print(to_lower_case("Llama"))