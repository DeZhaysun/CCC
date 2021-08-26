n = int(input())
if n!= 0 and n <= 10000:
    computer=[]
    spec = []

    for i in range(n):
        line = input()
        x = line.split()
        computer.append([x[0],2*int(x[1]) + 3*int(x[2]) + int(x[3])])
        spec.append(computer[i][1])

    spec.sort(reverse=True)

    for i in range(n):
        if spec[0] == computer[i][1]:
            name1 = computer[i][0]
            index = i
            break
    if n == 1:
        print(name1)
    elif n >= 2:
        for i in range(n):
            if spec[1] == computer[i][1] and i != index:
                name2 = computer[i][0]
                break

        if name1 < name2 and spec[0] == spec[1]:
            print(name1)
            print(name2)
        elif spec[0] == spec[1]:
            print(name2)
            print(name1)
        else:
            print(name1)
            print(name2)