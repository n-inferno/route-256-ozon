from collections import defaultdict


def get_int():
    return int(input())


def get_combinations(word):
    words = []
    for i in range(len(word) - 1, -1, -1):
        words.append(word[i:])
    words.append("")
    return words


def rhyme(word, dictionary):
    for i in range(len(word) + 1):
        if len(dictionary[word[i:]]) >= 1:
            for search_rhyme in dictionary[word[i:]]:
                if search_rhyme != word:
                    return search_rhyme


def main():
    n = get_int()
    dictionary = defaultdict(set)

    for _ in range(n):
        word = input()
        combinations = get_combinations(word)
        for cmb in combinations:
            dictionary[cmb].add(word)

    q = get_int()
    for _ in range(q):
        word = input()
        print(rhyme(word, dictionary))


if __name__ == '__main__':
    main()
