# 入力の例
# 3
# Aoki
# Takahashi
# Takahashi

def count_takahashi(n, strings):
    """
    与えられた文字列の中で「Takahashi」がいくつあるかを数える関数

    引数:
    n : int : 文字列の数
    strings : list : 文字列のリスト

    戻り値:
    int : 「Takahashi」の数
    """
    # "Takahashi"の数を数えるためのカウンタ
    count = 0

    # すべての文字列をチェック
    for string in strings:
        if string == "Takahashi":
            count += 1

    return count

# 標準入力からデータを読み取る部分
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    # 最初の入力は文字列の数N
    N = int(data[0])
    # 残りの入力は各文字列Si
    strings = data[1:]

    # 「Takahashi」の数を数える
    result = count_takahashi(N, strings)

    # 結果を出力
    print(result)

# 計算量についての説明:
# この関数はN個の文字列を1つずつチェックして、「Takahashi」に一致するかどうかを確認します。
# 各文字列の比較操作は定数時間O(1)で行われるため、N個の文字列全体をチェックする時間はO(N)となります。
# したがって、このアルゴリズムの計算量はO(N)です。
