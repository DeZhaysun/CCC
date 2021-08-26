def width(n, wide, total):
    if (total >= n):
        return wide
    else:
        total = total + wide
        if (total >= n):
            return wide
        else:
            total = total + wide
            if (total >= n):
                return wide
            else:
                wide += 1
                width(n,wide,total)

s = int(input("Start Value: "))
e = int(input("End Value: "))
d = e - s
w = 1
t = 0
wide = width(d,w,t)
