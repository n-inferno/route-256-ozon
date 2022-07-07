def get_int():
    return int(input())


def get_two_int():
    return list(map(int, input().split()))


def evaluate_map(game_map):
    seen_regions = set()
    steps = ((-1, -1), (-1, 1), (0, -2), (0, 2), (1, -1), (1, 1))

    seen = set()

    def helper(x, y, curr_region):
        nonlocal seen, steps
        if not (0 <= x < len(game_map)) or not (0 <= y < len(game_map[x])):
            return
        if (x, y) in seen:
            return

        if game_map[x][y] != curr_region:
            return

        seen.add((x, y))

        for dx, dy in steps:
            new_x, new_y = x + dx, y + dy
            helper(new_x, new_y, curr_region)

    for i in range(len(game_map)):
        for j in range(len(game_map[i])):
            curr_point = game_map[i][j]
            if curr_point in seen_regions and (i, j) not in seen:
                return False

            helper(i, j, curr_point)
            seen_regions.add(curr_point)

    return True


def main():
    sets = get_int()
    for _ in range(sets):
        m, _ = get_two_int()
        game_map = []
        for _ in range(m):
            game_map.append(list(input()))

        result = evaluate_map(game_map)
        print("YES" if result else "NO")


if __name__ == '__main__':
    main()
