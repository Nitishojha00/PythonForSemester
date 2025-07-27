def isPalindrome(s):
    l = len(s)
    l = l//2
    for i in range(0,l+1):
        if(s[i]!=s[len(s)-i-1]):
            return False

    return True;


s = input("Enter a string to check palindrome   :  ")
print(isPalindrome(s));