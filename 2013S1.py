y = int(input())
unique = True
x = y + 1
while(True):
    s = str(x)
    for i in range(len(s) - 1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                unique = False
                break
        if unique == False:
            break
    if unique:
        break       
    unique = True   
    x = x + 1
print(x)