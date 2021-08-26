maxOrMin = int(input())
n = int(input())
totalSpeeds = 0

line = input()
d = line.split()
d = [int(i) for i in d]

line = input()
p = line.split()
p = [int(i) for i in p]

if maxOrMin == 2:
    allSpeeds = d + p
    allSpeeds.sort(reverse = True)
    for i in range(n):
        totalSpeeds = allSpeeds[i] + totalSpeeds
elif maxOrMin == 1:
    d.sort()
    p.sort()
    for i in range(n):
        totalSpeeds = totalSpeeds + max(d[i],p[i])
print(totalSpeeds)