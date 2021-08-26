max = int(input())
initial = int(input())
infect = int(input())

spreaders = initial
nonspreaders = 0
day = 1

while(True):
    spreaders = spreaders * infect
    nonspreaders = nonspreaders + spreaders
    total = spreaders + nonspreaders
    if total > max:
        break
    day += 1

print(day)