n = int(input())

time = []
position = []
first = True

for i in range(n):
    line = input()
    x = line.split()
    time.append(int(x[0]))
    position.append(int(x[1]))

timeAndPosition = zip(time,position)
timeAndPosition = sorted(timeAndPosition)

for i in range(n-1):
    deltaT = timeAndPosition[i+1][0] - timeAndPosition[i][0]

    deltaP = abs(timeAndPosition[i+1][1] - timeAndPosition[i][1])

    speed = deltaP/deltaT
    if first:
        max = speed
        first = False
    if speed > max:
        max = speed
print(max)
