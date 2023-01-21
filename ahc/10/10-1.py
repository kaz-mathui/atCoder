import random
to = [
    [1, 0, -1, -1],
    [3, -1, -1, 0],
    [-1, -1, 3, 2],
    [-1, 2, 1, -1],
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [2, -1, 0, -1],
    [-1, 3, -1, 1],
]

next_tile = [1,2,3,0,5,4,7,6]
prev_tile = [3,0,1,2,5,4,7,6]

D = [(0,-1),(-1,0),(0,1),(1,0)]

group = [[0,1,2,3],[4,5],[6,7]]
group_index = [0,0,0,0,1,1,2,2]

def main():
    def calc_length(sy,sx,sd,is_checked):
        y,x = sy,sx
        direction = sd
        length = 0
        while 1:
            is_checked[y][x][direction] = 1
            length += 1
            direction = to[t[y][x]][direction^2]
            if direction < 0:
                return 0
            is_checked[y][x][direction^2] = 1
            dy,dx = D[direction]
            y += dy
            x += dx
            if y < 0 or n <= y or x < 0 or n <= x:
                return 0
            if sy == y and sx == x and sd == direction:
                return length

    def calc_score(t):
        is_checked = [[[0]*4 for _ in range(n)] for _ in range(n)]
        big = [0,0]
        for y in range(n):
            for x in range(n):
                for direction in range(4):
                    if is_checked[y][x][direction]:
                        continue
                    length = calc_length(y,x,direction,is_checked)
                    if big[0] < length:
                        big = [length, big[0]]
                    elif big[1] < length:
                        big[1] = length
        return big[0]*big[1]
    
    def dfs(sy,sx,sd,is_used):
        y,x,direction = sy,sx,sd
        stack = [[(y,x,direction,t[y][x])]]
        res = [(y,x,direction,t[y][x])]
        max_iterations = 10000
 
        iteration = 0
        while stack:
            iteration += 1
            route = stack.pop()
            if len(res) < len(route):
                res = route[:]
            if iteration >= max_iterations:
                return res
            y,x,direction,tyx = route[-1]
            nd = to[tyx][direction]
            dy,dx = D[nd]
            nd ^= 2
            ny,nx = y+dy,x+dx
            if ny < 0 or n <= ny or nx < 0 or n <= nx:
                continue
            if ny == sy and nx == sx and nd == sd:
                continue
            f = None
            for y_,x_,_,tyx in route:
                if ny == y_ and nx == x_:
                    f = tyx
                    break
            if not is_used[ny][nx] and f is None:
                for tnyx in group[group_indexes[ny][nx]]:
                    if to[tnyx][nd] >= 0:
                        stack.append(route+[(ny,nx,nd,tnyx)])
            else:
                if f is not None:
                    tnyx = f
                else:
                    tnyx = t[ny][nx]
                if to[tnyx][nd] >= 0:
                    stack.append(route+[(ny,nx,nd,tnyx)])
        return res
 
    def greedy():
        is_passed = [[[0]*4 for _ in range(n)] for _ in range(n)]
        is_used = [[0]*n for _ in range(n)]
        for sy in range(n):
            for sx in range(n):
                for sd in range(4):
                    if to[t[sy][sx]][sd] < 0 or is_passed[sy][sx][sd]:
                        continue
                    res = dfs(sy,sx,sd,is_used)
                    for y,x,direction,tyx in res:
                        t[y][x] = tyx
                        is_passed[y][x][direction] = 1
                        is_passed[y][x][to[tyx][direction]] = 1
                        is_used[y][x] = 1
        return

    # ランダムに見つける（最初：山登り的？）
    # n = 30
    # t = [list(map(int,input())) for _ in range(n)]
    # best = calc_score(t)
    # base_t = [ti[:] for ti in t]
    # T = [ti[:] for ti in t]
    # for _ in range(1000):
    #     for y in range(n):
    #         for x in range(n):
    #             t[y][x] = random.choice(group[group_index[t[y][x]]])
    #     score = calc_score(t)
    #     if best < score:
    #         best = score
    #         T = [ti[:] for ti in t]
    # t = [ti[:] for ti in T]

    # dfs的に閉路探索
    n =30
    t = [list(map(int,input())) for _ in range(n)]
    group_indexes = [[group_index[tyx] for tyx in ty] for ty in t]
    best = calc_score(t)
    base_t = [ti[:] for ti in t]
    greedy()

    # 近傍で操作して上がるかチェック、上がらなければ戻す（共通）
    for _ in range(1000):
        by = random.randrange(n)
        bx = random.randrange(n)
        for y in range(by-3,by+3):
            for x in range(bx-3,bx+3):
                if 0 <= y < n and 0 <= x < n and (y+x)&1:
                    t[y][x] = next_tile[t[y][x]]
        score = calc_score(t)
        if best < score:
            best = score
        else:
            for y in range(by-3,by+3):
                for x in range(bx-3,bx+3):
                    if 0 <= y < n and 0 <= x < n and (y+x)&1:
                        t[y][x] = prev_tile[t[y][x]]
    
    # 何回転させるかチェックする機構
    ans = []
    for y in range(n):
        for x in range(n):
            tyx = base_t[y][x]
            s = 0
            while tyx != t[y][x]:
                tyx = next_tile[tyx]
                s += 1
            ans.append(s)
    print(*ans,sep="")
    return

    
if __name__ == "__main__":
    main()
