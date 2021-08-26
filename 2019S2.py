import math 

def isPrime(n):
    prime= True
    count = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            count += 1
            if count > 1:
                prime = False
                break
    return prime

n = int(input())

output = []

for i in range(n):
    total = int(input()) * 2
    for j in range(2,total):
        if isPrime(j):
            prime1 = j
            if isPrime(total - j):
                output.append([j, total-j])
                break

for i in range(n):
    print(output[i][0], output[i][1])
