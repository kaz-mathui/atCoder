import time

def solution(N):
    bin_str = bin(N)
    print(bin_str)
    bin_main = bin_str[2:]
    print(bin_main)
    counter, max_gap = 0, 0
    flag = False
    for s in bin_main[::-1]:
        print(s)
        if s == "1":
            if 0 < counter:
                if max_gap < counter:
                    max_gap = counter
            counter = 0
            flag = True
        else:
            if flag:
                counter += 1

    return max_gap

def main():
    actual1 = solution(10)
    assert actual1 == 2, "actual: {} expected {}".format(actual1, 2)
    # print("test1")
    # actual1 = solution(9)
    # assert actual1 == 2, "actual: {} expected {}".format(actual1, 2)

    # print("test2")
    # actual2 = solution(529)
    # assert actual2 == 4, "actual: {} expected {}".format(actual2, 4)

    # print("test3")
    # actual3 = solution(20)
    # assert actual3 == 1, "actual: {} expected {}".format(actual3, 1)

    # print("test4")
    # actual4 = solution(15)
    # assert actual4 == 0,  "actual: {} expected {}".format(actual4, 0)

    # print("test5")
    # actual5 = solution(32)
    # assert actual5 == 0,  "actual: {} expected {}".format(actual5, 0)

    # print("test6")
    # actual6 = solution(1041)
    # assert actual6 == 5, "actual: {} expected {}".format(actual6, 5)

    # print("test7")
    # start = time.time()
    # actual7 = solution(2147483647)
    # print("calculation time: {}".format(time.time() - start))
    # assert actual7 == 0, "actual: {} expected {}".format(actual7, 0)


if __name__ == "__main__":
    main()