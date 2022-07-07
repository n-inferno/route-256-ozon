from collections import defaultdict


def get_two_int():
    return list(map(int, input().split()))


def main():
    users, req = get_two_int()

    users_map = defaultdict(int)
    request_counter = 0
    last_broadcast = 0

    for r in range(req):
        t, usr_id = get_two_int()
        if t == 1:
            if usr_id == 0:
                request_counter += 1
                last_broadcast = request_counter
            else:
                request_counter += 1
                users_map[usr_id] = request_counter
        elif t == 2:
            print(max(users_map[usr_id], last_broadcast))


if __name__ == '__main__':
    main()
