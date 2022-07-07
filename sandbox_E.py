from collections import defaultdict, deque


class UniqueLimitedQueue:
    def __init__(self):
        self.queue = deque()
        self.elements = set()

    def add(self, element):
        self.queue.append(element)
        if element in self.elements:
            for it in range(len(self.queue)):
                if self.queue[it] == element:
                    break
            del self.queue[it]
        else:
            if len(self.queue) > 5:
                ex_element = self.queue.popleft()
                self.elements.discard(ex_element)
            self.elements.add(element)

    @property
    def size(self):
        return len(self.queue)

    @property
    def values(self):
        return list(self.queue)[::-1]


if __name__ == '__main__':
    num = int(input())
    for _ in range(num):
        journal_entries = int(input())
        phone_book = defaultdict(UniqueLimitedQueue)
        for entry in range(journal_entries):
            name, phone = input().split()
            phone_book[name].add(phone)

        for item in sorted(phone_book):
            print(f"{item}: {phone_book[item].size}", end=" ")
            print(*phone_book[item].values)
        print()
