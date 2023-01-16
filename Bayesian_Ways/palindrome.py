
# 1. Check if the given string is a palindrome or not irrespective of case

def palindrome(string):
    s = string[::-1].lower()
    if string.lower() == s:
        print('It is Palindrome')
    else:
        print('It is not a Palindrome')


word = input('Enter Word which want to check Palindrome or not : ')
palindrome(word)