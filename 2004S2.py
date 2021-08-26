x = input()
x = x.split()
n = int(x[0])
k = int(x[1])
score = [0] * n
rank = k*[n*[0]]

for i in range(k):
    x = input()
    x = x.split()
    for j in range(n):
        score[j] = int(x[j]) + score[j]

    sortedScores = sorted(score, reverse = True)
    
    for j in range(n):
        for x in range(n):
            if score[j] == sortedScores[x]:
                rank[i][j] = x + 1

highestScore = score[0]
position = 1
for i in range(1, n):
    if score[i] > highestScore:
        highestScore = score[i]
        position = i + 1

lowestRank = rank[0][position - 1]

for i in range(1, k):
    if rank[i][position-1] > lowestRank:
        lowestRank = rank[i][position-1]

print("Yodeller ", position," is the TopYodeller: score ", highestScore, " worst rank ", lowestRank)
    
            

    

    
    