max = int(input())
n = int(input())
w = [0] * (n+3)
count = 0

for i in range(3,n+3):
    w[i] = int(input())

for i in range(n):
    t= w[i] + w[i+1] + w[i+2] + w[i+3]
    if(t>max):
        break
    count += 1
print(count)