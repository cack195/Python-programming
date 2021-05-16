def read_matrix(r,c,m):
    for i in range(r):
        m.append([])
        for j in range(c):
            x = int(input())
            m[i].append(x)

def add_matrix(r,c,m1,m2,m3):
    for i in range(r):
        m3.append([])
        for j in range(c):
            y = m1[i][j]+m2[i][j]
            m3[i].append(y)

def print_matrix(r,c,m):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end='')
            print()

r = int(input())
c = int(input())
m1 = []
m2 = []
m3 = []
read_matrix(r,c,m1)
read_matrix(r,c,m2)
add_matrix(r,c,m1,m2,m3)
for i in range(r):
    print(m3[i])






