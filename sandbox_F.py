import bisect

SUCCESS = "SUCCESS"
FAIL = "FAIL"

# 1 - first not free, 2 - second not free, 0 - all free, 3 - all busy


def _get_coupe(n):
    return ((n - 1) // 2) + 1


def _get_places(n):
    return f" {(n * 2) - 1}-{n * 2}"


def buy(num, coupes, free):
    coupe = _get_coupe(num)
    place = 1 if num % 2 == 1 else 2
    if coupes[coupe] in (place, 3):
        return FAIL
    coupes[coupe] = place if coupes[coupe] == 0 else 3
    if coupes[coupe] == place:
        free.pop(bisect.bisect_left(free, coupe))
    return SUCCESS


def refund(num, coupes, free):
    coupe = _get_coupe(num)
    place = 2 if num % 2 == 1 else 1
    if coupes[coupe] in (place, 0):
        return FAIL
    coupes[coupe] = 0 if coupes[coupe] != 3 else place
    if coupes[coupe] == 0:
        free.insert(bisect.bisect_left(free, coupe), coupe)
    return SUCCESS


def buy_coupe(coupes, free):
    try:
        cp = free.pop(0)
    except IndexError:
        return FAIL
    coupes[cp] = 3
    return SUCCESS + _get_places(cp)


if __name__ == '__main__':
    i = 0
    num = int(input())
    results = []
    for _ in range(num):
        input()
        coupes, samples = input().split()

        coupes_map = {i: 0 for i in range(1, int(coupes) + 1)}
        free = [i for i in range(1, int(coupes) + 1)]

        for sample in range(int(samples)):
            operations = input().split()
            if len(operations) == 2:
                if operations[0] == "1":
                    result = buy(int(operations[1]), coupes_map, free)
                elif operations[0] == "2":
                    result = refund(int(operations[1]), coupes_map, free)
                else:
                    raise NotImplementedError
            else:
                result = buy_coupe(coupes_map, free)
            print(result)
            i += 1
        print()
