# 2. The user enters a string and a substring. You have to print the number of times that the
# substring occurs in the given string. String traversal will take place from left to right, not from
# right to left.
# NOTE: String letters are case-sensitive. The first line of input contains the original string. The
# next line contains the substring
import re


def sub_string(s, sub):
    n = re.findall(sub, s)
    print(f'Output : {len(n)}')


string = input('Input : ')
pattern = input('pattern : ')
sub_string(string, pattern)
