from collections import defaultdict


def get_two_int():
    return list(map(int, input().split()))


def get_recommendations(friends_list):
    rec = defaultdict(list)
    for person, friends in friends_list.items():
        counter = {}
        max_counter = 0
        for friend in friends:
            if friend == person:
                continue
            for friends_friend in friends_list[friend]:
                if friends_friend in friends or friends_friend == person:
                    continue
                if friends_friend in counter:
                    counter[friends_friend] += 1
                else:
                    counter[friends_friend] = 1

                max_counter = max(max_counter, counter[friends_friend])

        for psn, count in counter.items():
            if count == max_counter:
                rec[person].append(psn)

    return rec


def main():
    n, m = get_two_int()
    friends_list = {k: set() for k in range(1, n + 1)}
    for _ in range(m):
        f1, f2 = get_two_int()
        friends_list[f1].add(f2)
        friends_list[f2].add(f1)

    rec = get_recommendations(friends_list)
    for i in range(1, n + 1):
        if not rec[i]:
            print(0)
        else:
            print(*sorted(rec[i]))


if __name__ == '__main__':
    main()
