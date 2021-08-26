pinkCost = int(input())
greenCost = int(input())
redCost = int(input())
orangeCost = int(input())
money = int(input())
count = 0
first = True

for o in range(int(money/orangeCost) + 1):
    for r in range(int(money/redCost) + 1):
        for g in range(int(money/greenCost)+1):
            for p in range(int(money/pinkCost)+1):
                if o*orangeCost + r*redCost + g*greenCost + p*pinkCost == money:
                    count += 1
                    print("# of PINK is",p,"# of GREEN is",g,"# of RED is",r,"# of ORANGE is",o)
                    if first:
                        minimum = o + r + g + p
                        first = False
                    if o + r + g + p < minimum:
                        minimum = o + r + g + p
print("Total combinations is "+str(count)+".")
print("Minimum number of tickets to print is "+str(minimum)+".")