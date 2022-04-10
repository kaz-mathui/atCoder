A,B,C = map(int,input().split())

if A % 10 == 1 or A % 10 == 5 or A % 10 == 6 or A % 10 == 0:
    print(A%10)
    exit()

# bigNum = B**C

# B**Cのmod4を求める

b_mod4 = B % 4

if b_mod4 == 1:
    bigNum = 1
if b_mod4 == 2:
    if C % 4 == 1:
        bigNum = 2
    if C % 4 == 2:
        bigNum = 4
    if C % 4 == 3:
        bigNum = 8
    if C % 4 == 0:
        bigNum = 6
if b_mod4 == 3:
    if C % 4 == 1:
        bigNum = 3
    if C % 4 == 2:
        bigNum = 9
    if C % 4 == 3:
        bigNum = 7
    if C % 4 == 0:
        bigNum = 1
if b_mod4 == 0:
    bigNum = 0





if A % 10 == 9 or A % 10 == 4:
    if bigNum % 2 == 0 :
        if A % 10 == 4:
            print(6)
        else:
            print(1)
    else:
        if A % 10 == 4:
            print(4)
        else:
            print(9)

    exit()

if A % 10 == 2:
    if bigNum % 4 == 0:
        print(6)
    elif bigNum % 4 == 1:
        print(2)
    elif bigNum % 4 == 2:
        print(4)
    else:
        print(8)
    exit()
    

if A % 10 == 3:
    if bigNum % 4 == 0:
        print(1)
    elif bigNum % 4 == 1:
        print(3)
    elif bigNum % 4 == 2:
        print(9)
    else:
        print(7)
    exit()

if A % 10 == 7:
    if bigNum % 4 == 0:
        print(1)
    elif bigNum % 4 == 1:
        print(7)
    elif bigNum % 4 == 2:
        print(9)
    else:
        print(3)
    exit()


if A % 10 == 8:
    if bigNum % 4 == 0:
        print(6)
    elif bigNum % 4 == 1:
        print(8)
    elif bigNum % 4 == 2:
        print(4)
    else:
        print(2)
    exit()