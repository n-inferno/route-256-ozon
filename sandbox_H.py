class InvalidShip(Exception):
    pass


STEPS = ((0, 1), (0, -1), (1, 0), (-1, 0))  # right left down up
STEP_TO_DIR = {(0, 1): "r", (0, -1): "l", (1, 0): "d", (-1, 0): "u"}
DIR_TO_STEP = {k: v for v, k in STEP_TO_DIR.items()}
STEPS_DIAGONAL = ((1, 1), (-1, -1), (1, -1), (-1, 1))


def check_ship_mid(x, y, field, res):
    if not 0 <= x < len(field) or not 0 <= y < len(field[0]) or field[x][y] == ".":
        return ""

    return res


def check_ship_corners(ship_points, seen, field):
    for x, y in ship_points:
        for dx, dy in STEPS_DIAGONAL + STEPS:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(field) and 0 <= new_y < len(field[0]):
                if (new_x, new_y) in ship_points or field[new_x][new_y] == ".":
                    seen.add((new_x, new_y))
                else:
                    raise InvalidShip


def check_ship(s, x, y, field):
    directions = (DIR_TO_STEP[ch] for ch in s)

    results = []
    points = set()
    for dx, dy in directions:
        new_x, new_y = x, y
        r = 0
        while 0 <= new_x < len(field) and 0 <= new_y < len(field[0]) and field[new_x][new_y] == "*":
            points.add((new_x, new_y))
            r += 1
            new_x += dx
            new_y += dy

        results.append(r)

    assert len(results) == 2

    if results[0] != results[1] or results[0] > 4:
        raise InvalidShip

    return results[0] * 2 - 1, points


def check(field):
    seen = set()
    ships = []

    stars = set()

    for i in range(len(field)):
        for j in range(len(field[i])):
            if (i, j) in seen or field[i][j] == ".":
                continue

            s = ""
            for dx, dy in STEPS:
                s += check_ship_mid(i + dx, j + dy, field, STEP_TO_DIR[(dx, dy)])

            if not s:
                check_ship_corners({(i, j)}, seen, field)
                stars.discard((i, j))
                decks = 1
                ships.append(decks)
            elif s in ("ru", "rd", "lu", "ld"):
                decks, points = check_ship(s, i, j, field)
                stars -= points
                check_ship_corners(points, seen, field)
                ships.append(decks)
            elif len(s) > 2:
                raise InvalidShip
            else:
                stars.add((i, j))

    if stars:
        raise InvalidShip

    ships.sort()
    return ships


def main():
    num = int(input())
    for _ in range(num):
        row, col = list(map(int, input().split()))
        field = []
        for _ in range(row):
            field.append(list(input()))

        try:
            result = check(field)
        except InvalidShip:
            print("NO")
        else:
            print("YES")
            print(*result)


if __name__ == '__main__':
    main()
