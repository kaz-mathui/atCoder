S=lambda:input().split()
M=lambda:map(int,input().split())
L=lambda:list(map(int,input().split()))
O=lambda:map(int,open(0).read().split())
 
def main():
    a=L()
    if len(set(a)) == 2:
        if a.count(a[0]) in (2,3):
            print("Yes")
            return
    print("No")
    return

if __name__ == "__main__":
    main()