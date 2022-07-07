def get_int():
    return int(input())


def get_list_int():
    return list(map(int, input().split()))


def get_pairs(devs):
    devs = list(enumerate(devs, start=1))
    pairs = []

    while len(devs) > 1:
        min_diff = float("inf")
        min_index = 0
        curr_dev = 1

        while curr_dev < len(devs):
            curr_diff = abs(devs[0][1] - devs[curr_dev][1])
            if curr_diff < min_diff:
                min_diff = curr_diff
                min_index = curr_dev
            curr_dev += 1

        pairs.append([devs[0][0], devs[min_index][0]])
        devs.pop(min_index)
        devs.pop(0)

    return pairs


def main():
    t = get_int()
    for i in range(t):
        input()
        devs = get_list_int()
        pairs = get_pairs(devs)

        for pair in pairs:
            print(*pair)
        print()


if __name__ == '__main__':
    main()
