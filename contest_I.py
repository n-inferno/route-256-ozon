import heapq


def get_two_int():
    return list(map(int, input().split()))


def get_list_int():
    return get_two_int()


def get_list():
    return input().split()


def calculate(processors_spend_energy, tasks, processors):
    sum_spend = 0
    to_free_procs = []

    for time_come, time_execute in tasks:
        while to_free_procs and time_come >= to_free_procs[0][0]:
            _, proc_id = heapq.heappop(to_free_procs)
            heapq.heappush(processors_spend_energy, (processors[proc_id - 1], proc_id))

        try:
            free_proc = heapq.heappop(processors_spend_energy)
        except IndexError:
            continue

        heapq.heappush(to_free_procs, (time_come + time_execute, free_proc[1]))
        sum_spend += (free_proc[0] * time_execute)

    return sum_spend


def main():
    processors, m = get_two_int()
    processors_lst = get_list_int()
    processors_spend_energy = [(n, i) for i, n in enumerate(processors_lst, start=1)]
    heapq.heapify(processors_spend_energy)

    tasks = []
    for _ in range(m):
        tasks.append(get_two_int())

    print(calculate(processors_spend_energy, tasks, processors_lst))


if __name__ == '__main__':
    main()
