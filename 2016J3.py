def isPalindrome(s):
    palindrome = True
    for i in range(int(len(s)/2+1)):
        if i != len(s)- 1 - i:
            if s[i] != s[len(s)-1-i]:
                palindrome = False
                break
    return palindrome

s = input()
max = 0
for i in range(len(s)):
    for j in range(1, len(s)-i+1):
        if isPalindrome(s[i:i+j]):
            if len(s[i:j+i]) > max:
                max = len(s[i:i+j])

print(max)