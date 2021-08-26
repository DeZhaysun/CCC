row = int(input())
column = int(input())
table = []
found = False

for i in range(row):
    line = input()
    c = line.split()
    c = [int(i) for i in c]

    table.append(c)

def search(v,r,c):
    if table[0][0] == v:
        return True
    for i in range(r):
        for j in range(c):
            if table[i][j] == v:
                if i == 0 and j == 0:
                    return True
                else:
                    v = (i+1) * (j + 1)
                    print(i+1,j+1)
                    print(v)
                    search(v,r,c)


value = row * column

search(value,row,column)

