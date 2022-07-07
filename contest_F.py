def get_int():
    return int(input())


def validate(timeline, i1, i2):
    h1, m1, s1 = list(map(int, i1.split(":")))
    h2, m2, s2 = list(map(int, i2.split(":")))

    for h in (h1, h2):
        if h not in range(0, 24):
            return False

    for ms in (m1, s1, m2, s2):
        if ms not in range(0, 60):
            return False

    if h2 < h1:
        return False
    elif h2 == h1:
        if m2 < m1:
            return False
        elif m2 == m1:
            if s2 < s1:
                return False

    timeline_index_1 = h1 * 3600 + m1 * 60 + s1
    timeline_index_2 = h2 * 3600 + m2 * 60 + s2

    for i in range(timeline_index_1, timeline_index_2 + 1):
        if timeline[i]:
            return False
        timeline[i] = 1

    return True


def main():
    sets = get_int()
    for _ in range(sets):
        n = get_int()
        timeline = [0] * (86400 + 1)
        result = True
        for _ in range(n):
            intervals = input().split("-")
            if result:
                if not validate(timeline, *intervals):
                    result = False

        print("YES" if result else "NO")


if __name__ == '__main__':
    main()
