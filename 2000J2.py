start = int(input())
end = int(input())
count = 0
newS = ""

for i in range(start, end+1):
    s = str(i)
    for j in range(len(s)-1, -1, -1):
        if s[j] == "1" or s[j] == "0" or s[j] == "8":
            newS = newS + s[j]
        elif s[j] == "6":
            newS = newS + "9"
        elif s[j] == "9":
            newS = newS + "6" 
        else:
            break
    if s == newS:
        count += 1
    newS = ""

print(count)