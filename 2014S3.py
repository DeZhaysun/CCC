tests = int(input())
answers = [""] * tests

for i in range(tests):
    n = int(input())

    mountainTopIndex = n-1
    branch = []
    branchIndex = -1
    count = 1
    mountainTop = []

    for j in range(n):
        x = int(input())
        mountainTop.append(x)

    while True:
        if len(mountainTop) == 0 and len(branch) == 0:
            answers[i] = "Y"
            break
        elif len(mountainTop) == 0 and branch[branchIndex] != count:
            answers[i] = "N"
            break
        elif len(branch) > 0 and branch[branchIndex] == count:
            branch.pop()
            branchIndex -= 1
            count += 1
        elif mountainTop[mountainTopIndex] == count:
            mountainTop.pop()
            mountainTopIndex -= 1
            count += 1
        else:
            branch.append(mountainTop[mountainTopIndex])
            mountainTop.pop()
            mountainTopIndex -= 1
            branchIndex += 1

for i in range(tests):
    print(answers[i])