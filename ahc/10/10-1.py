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

next_direction = [2,3,0,1]

next_tile = [1,2,3,0,5,4,7,6]
prev_tile = [3,0,1,2,5,4,7,6]

D = [(0,-1),(-1,0),(0,1),(1,0)]

group = [[0,1,2,3],[4,5],[6,7]]
group_index = [0,0,0,0,1,1,2,2]

def main():
    # 長さを計算
    def calc_length(sy,sx,sd,is_checked):
        y,x = sy,sx
        direction = sd
        length = 0
        while 1:
            # 通ったところに印
            is_checked[y][x][direction] = 1
            length += 1
            if direction < 0:
                return 0
            direction = to[t[y][x]][next_direction[direction]]
            is_checked[y][x][next_direction[direction]] = 1
            dy,dx = D[direction]
            y += dy
            x += dx
            # 範囲を越えちゃったら長さ0
            if y < 0 or n <= y or x < 0 or n <= x:
                return 0
            # 元の位置に戻ってきたら長さ返して終わり
            if sy == y and sx == x and sd == direction:
                return length

    def calc_score():
        is_checked = [[[0]*4 for _ in range(n)] for _ in range(n)]
        big = [0,0]
        for y in range(n):
            for x in range(n):
                for direction in range(4):
                    # if 0 = if false 通ってるなら　continue　つまり別のループのタイミングで計算しているのでここではスキップ
                    if is_checked[y][x][direction]:
                        continue
                    length = calc_length(y,x,direction,is_checked)
                    if big[0] < length:
                        big = [length, big[0]]
                    elif big[1] < length:
                        big[1] = length
        return big[0]*big[1]
    
    # s：最初のやつ
    def dfs(sy,sx,sd,is_used):
        y,x,direction = sy,sx,sd
        stack = [[(y,x,direction,t[y][x])]]
        res = [(y,x,direction,t[y][x])]
        max_iterations = 10000
 
        iteration = 0
        while stack:
            iteration += 1
            route = stack.pop()
            # responseがrouteより小さければ一旦routeにしちゃう。
            if len(res) < len(route):
                res = route[:]
            if iteration >= max_iterations:
                return res
            # ルートの先端にあるタイルを取り出す
            y,x,direction,tyx = route[-1]
            # n系ネクスト。
            nd = to[tyx][direction]
            dy,dx = D[nd]
            nd = next_direction[nd]
            ny,nx = y+dy,x+dx
            # オーバーしたらコンティニュー
            if ny < 0 or n <= ny or nx < 0 or n <= nx:
                continue
            # 最初に戻ってきたらコンティニュー
            if ny == sy and nx == sx and nd == sd:
                continue
            f = None
            # routeの中からの中から場所と方向,タイルの種類を取り出す
            for y_,x_,_,tyx in route:
                # 次に進む状態と、今までのルートのうちどこかに、同じ状態があるなら
                if ny == y_ and nx == x_:
                    # fにその状態のタイルを記録
                    f = tyx
                    break
            # if 0 = if false
            # まだ使われてないかつ、fに種類を記録されてない（つまり、今までのルートと同じ状態のものが存在しない）→新しい場所を開拓中。なら
            if not is_used[ny][nx] and f is None:
                # 同じ種類グループの中で試す。（回転してどうにかできないか？）
                for tnyx in group[group_indexes[ny][nx]]:
                    # 今の方向から侵入可能なタイルなら
                    if to[tnyx][nd] >= 0:
                        # routeにtupleとして追加してstackに戻す。全ての場合を記録しておく
                        stack.append(route+[(ny,nx,nd,tnyx)])
            else:
                # もうその場所がルートとして使われているかつ現在探してるルートにも同じものがある、つまりここまでの探索が限界。。。
                # 限界なので行き止まったとこの種類を最終のタイルとする
                if f is not None:
                    tnyx = f
                # もうその場所が使われているかつfに入っていない
                # 使われているけど、現在のルートはスムーズにきているからスタックにためて一旦終わる
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
                    # もらってきたレスポンスのルートをis_passedとis_usedに記録する
                    for y,x,direction,tyx in res:
                        t[y][x] = tyx
                        is_passed[y][x][direction] = 1
                        is_passed[y][x][to[tyx][direction]] = 1
                        is_used[y][x] = 1
        return

    # # ランダムに見つける（最初：山登り的）→19996点
    # n = 30
    # t = [list(map(int,input())) for _ in range(n)]
    # best = calc_score()
    # base_t = [ti[:] for ti in t]
    # T = [ti[:] for ti in t]
    # for _ in range(1000):
    #     for y in range(n):
    #         for x in range(n):
    #             # ランダムにタイルを変更する
    #             t[y][x] = random.choice(group[group_index[t[y][x]]])
    #     score = calc_score()
    #     # 上回ってたらラッキーこっち選択
    #     if best < score:
    #         best = score
    #         T = [ti[:] for ti in t]
    # t = [ti[:] for ti in T]

    # # dfs的に閉路探索　→ 352376　点
    # n = 30
    # t = [list(map(int,input())) for _ in range(n)]
    # # タイルの種類グループを記録する配列
    # group_indexes = [[group_index[tyx] for tyx in ty] for ty in t]
    # best = calc_score()
    # # 最初のタイルを記録しておく
    # base_t = [ti[:] for ti in t]
    # greedy()

    # 3つ目　チェックを入れることと回転それぞれを回転させて点数が上がらないか試行錯誤→1774092点
    # 2→20にすると
    n = 30
    t = [list(map(int,input())) for _ in range(n)]
    group_indexes = [[group_index[tyx] for tyx in ty] for ty in t]
    base_t = [ti[:] for ti in t]
    greedy()
    is_checked = [[[0]*4 for _ in range(n)] for _ in range(n)]
    # 20はキメ
    for _ in range(20):
        max_ = 0
        argmax = None
        for y in range(n):
            for x in range(n):
                # どっかから通られてたらスルー
                if sum(is_checked[y][x]):
                    continue
                # タイル種類を取得
                g = group[group_indexes[y][x]]
                # 今のタイル種類
                # calc_lengthで使うために一度tmpに入れておく
                temp = t[y][x]
                # 同じタイル種類のうち一つを選択
                for tyx in g:
                    # is_checkedを複製
                    is_checked_ = [[j[:] for j in i] for i in is_checked]
                    # 回転
                    t[y][x] = tyx
                    for d in range(4):
                        # 通ってたらcontinue
                        if is_checked[y][x][d]:
                            continue
                        l = calc_length(y,x,d,is_checked_)
                        # 回転させて長さが長くなったら記録する
                        if max_ < l:
                            max_ = l
                            argmax = (y,x,tyx,d)
                t[y][x] = temp
        # print(argmax)
        # argmaxに入らない時にエラーになる。のでこれが欲しい
        if max_ == 0:
            break
        y,x,tyx,d = argmax
        t[y][x] = tyx
        # 通ったところにチェックをつけることを忘れずに。
        calc_length(y,x,d,is_checked)
    best = calc_score()
    
    # 近傍の調べる範囲
    w = 0
    # 近傍で操作して上がるかチェック、上がらなければ戻す（共通）→10%くらい上がる
    for _ in range(1000):
        by = random.randrange(n)
        bx = random.randrange(n)
        for y in range(by-w,by+w+1):
            for x in range(bx-w,bx+w+1):
                # (y+x)&1 → 奇数ならtrue 偶数ならfalse if 0 = false
                # 範囲内かつ、x+yが奇数であることを確認している？？
                if 0 <= y < n and 0 <= x < n and (y+x)&1:
                    t[y][x] = next_tile[t[y][x]]
        score = calc_score()
        if best < score:
            best = score
        else:
            for y in range(by-w,by+w+1):
                for x in range(bx-w,bx+w+1):
                    if 0 <= y < n and 0 <= x < n and (y+x)&1:
                        t[y][x] = prev_tile[t[y][x]]
    
    # 何回転させるかチェックする
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
