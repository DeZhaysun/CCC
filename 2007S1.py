n = int(input())
output = []
for i in range(n):
    line = input()
    x = line.split()
    year = int(x[0])
    month = int(x[1])
    day = int(x[2])
    if year < 1989:
        output.append("Yes")
    elif year > 1989:
        output.append("No")
    else:
        if month < 2:
            output.append("Yes")
        elif month > 2:
            output.append("No")
        else:
            if day > 27:
               output.append("No")
            else:
                output.append("Yes") 
for i in range(n):
    print(output[i])
