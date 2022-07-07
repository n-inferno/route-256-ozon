def make_click(table, click):
    table.sort(key=lambda rw: rw[click - 1])


if __name__ == '__main__':
    num = int(input())
    for _ in range(num):
        input()
        row, col = input().split()
        table = []
        for _ in range(int(row)):
            table.append(list(map(int, input().split())))

        input()
        clicks = list(map(int, input().split()))
        previous = None
        for click in clicks:
            if click == previous:
                continue
            make_click(table, click)
            previous = click

        for i in range(int(row)):
            print(*table[i])
        print()
