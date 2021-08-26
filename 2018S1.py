n = int(input())
first = True
positions = []

for i in range(n):
    positions.append(int(input()))

positions.sort()

for i in range(1, n-1):
    size = (positions[i] - positions[i-1])/2 + (positions[i+1] - positions[i])/2
    if first:
        smallest = size
        first = False
    if size < smallest:
        smallest = size
print(round(smallest,1))