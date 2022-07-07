from collections import defaultdict


def get_price(goods):
    counter = defaultdict(int)
    total = 0
    for good in goods:
        counter[good] += 1
        if counter[good] == 3:
            counter[good] = 0
        else:
            total += good
    return total


if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        input()
        goods = list(map(int, input().split()))
        print(get_price(goods))
