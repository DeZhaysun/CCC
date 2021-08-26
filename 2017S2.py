n = int(input())
line = input()

level = line.split()
level = [int(i) for i in level]
low = True

level.sort()
if n%2==0:
    currentHigh = int(n/2)
    currentLow = int(n/2) - 1
    even = True
else:
    currentHigh = int(n/2)+1
    currentLow = int(n/2)
    even = False

while(True):
    if (low == True):
        print (level[currentLow], end = '')
        if (even == False):
            if (currentLow == 0):
                break
        print (" ", end = '')
        currentLow -= 1
        low = False
    else:
        print (level[currentHigh], end = '')
        if (even == True):
            if (currentHigh == n-1):
                break
        print (" ", end = '')
        currentHigh += 1
        low = True
