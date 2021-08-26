n = int(input())

line = input()
person = line.split()

line2 = input()
partner = line2.split()
correct= True

for i in range(n):
    if person[i] == partner[i]:
        correct = False
        break
    for j in range(n):
        if(person[i] == partner[j]):
            if not(partner[i] == person[j]):
                correct = False
                break
    if(correct == False):
        break

if(correct):
    print("good")
else:
    print("bad")
