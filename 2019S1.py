s = input()

x1 = [1,2]
x2 = [3,4]

for i in s:
    if i == 'H':
        swap = x1[0]
        x1[0] = x2[0]
        x2[0] = swap
        
        swap = x1[1]
        x1[1] = x2[1]
        x2[1] = swap
    else:
        swap = x1[0]
        x1[0] = x1[1]
        x1[1] = swap 

        swap = x2[0]
        x2[0] = x2[1]
        x2[1] = swap

print(x1[0],x1[1])
print(x2[0],x2[1]) 