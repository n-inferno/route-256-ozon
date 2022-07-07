def get_int():
    return int(input())


def get_list_int():
    return list(map(int, input().split()))


def evaluate(report):
    seen = set()
    prev = report[0]
    for entry in report:
        if entry in seen and entry != prev:
            return False
        seen.add(entry)
        prev = entry
    return True


def main():
    sets = get_int()
    for _ in range(sets):
        input()
        report = get_list_int()
        print("YES" if evaluate(report) else "NO")


if __name__ == '__main__':
    main()
