n = int(input())

line = input()
larry = line.split()
larry = [int(i) for i in larry]

line2 = input()
opponent = line2.split()
opponent = [int(i) for i in opponent]

battle = False
count = 0

for i in range(n):
    if larry[i] == opponent[i] and battle == False:
        battle = True
        count += 1
    elif larry[i] != opponent[i] and battle == True:
        battle = False

print(count)