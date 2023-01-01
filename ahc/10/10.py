from time import perf_counter
import random
TIME_LIMIT = 1.8

def resolve():
    start = perf_counter()
    H = W = 30
    tiles = [list(map(int, input())) for _ in range(H)]
    to = ((1, 0, -1, -1),
          (3, -1, -1, 0),
          (-1, -1, 3, 2),
          (-1, 2, 1, -1),
          (1, 0, 3, 2),
          (3, 2, 1, 0),
          (2, -1, 0, -1),
          (-1, 3, -1, 1),)
    # 次の状態の配列
    nxt = (1, 2, 3, 0, 5, 4, 7, 6)
    ans = [[0] * W for _ in range(H)]
    di = (0, -1, 0, 1)
    dj = (-1, 0, 1, 0)
    cnt = 0
    maxans = 0
    while perf_counter() - start <= TIME_LIMIT:
        cnt += 1
        i = random.randint(0, H - 1)
        j = random.randint(0, W - 1)
        # random要素。
        d = random.randint(1, 3) if tiles[i][j] < 4 else 1
        # dを決めてから、d回転させるかそのままかでどっちでやったほうが良さげかを比較する。
        before = []
        # 全ての方向から入ってきた場合を考える
        for dx in range(4):
            x, y, z = i, j, dx
            count = 0
            # ループの長さをカウントする
            while True:
                d2 = to[tiles[x][y]][z]
                if d2 == -1:
                    count = 0
                    break
                x += di[d2]
                y += dj[d2]
                if not 0 <= x < H or not 0 <= y < W:
                    count = 0
                    break
                z = (d2 + 2) % 4
                count += 1
                # ループが戻ってきた。
                if x == i and y == j and z == dx:
                    break
            if count > 0:
                before.append(count)
        before.sort(reverse=True)
        # キメのdだけ回転させる
        for _ in range(d):
            tiles[i][j] = nxt[tiles[i][j]]
        # ループがなかった or (今までの最高のループの20%に満たなかった and 20％の確率)であれば一旦回転を確定させて次の座標にいく。
        if not before or (before[0] <= maxans // 5 and random.random() < 0.2):
            ans[i][j] += d
            ans[i][j] %= 4
            continue
        # おんなじことをする
        after = []
        for dx in range(4):
            x, y, z = i, j, dx
            count = 0
            while True:
                d2 = to[tiles[x][y]][z]
                if d2 == -1:
                    count = 0
                    break
                x += di[d2]
                y += dj[d2]
                if not 0 <= x < H or not 0 <= y < W:
                    count = 0
                    break
                z = (d2 + 2) % 4
                count += 1
                if x == i and y == j and z == dx:
                    break
            if count > 0:
                after.append(count)
        after.sort(reverse=True)
        # 前のものより良い結果であれば採用する。
        if after > before:
            ans[i][j] += d
            ans[i][j] %= 4
            maxans = max(maxans, after[0])
        else:
            # 微妙だったので前の状態に戻す。
            for _ in range(4 - d):
                tiles[i][j] = nxt[tiles[i][j]]

    for x in ans:
        print("".join(map(str, x)), end="")
    print()


if __name__ == '__main__':
    resolve()
