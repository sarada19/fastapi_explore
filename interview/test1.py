import os 
from typing import List
input_arr = ['abcd', 'abc','abef']
# output_st = "ab"

def findLongestCommonStrUsingOS(arr: List[str]) -> str:
    return os.path.commonprefix(arr)

def find_longest_common_str(arr: List[str])-> str:
    str1 = min(arr)
    str2 = max(arr)
    for i, c in enumerate(str1):
        if c != str2[i]:
            return str1[:i]
    return str1
    
print(find_longest_common_str(input_arr))
print(findLongestCommonStrUsingOS(input_arr), "==============using OS")

