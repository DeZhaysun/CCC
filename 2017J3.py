line = input()
start = line.split()
start = [int(i) for i in start]

lineTwo = input()
destination = lineTwo.split()
destination = [int(i) for i in destination]

moves = int(input())

distance = abs(destination[0] - start[0]) + abs(destination[1] - start[1])
remainder = moves - distance

if(remainder%2 == 0) and (remainder >= 0):
    print("Y")
else:
    print("N")