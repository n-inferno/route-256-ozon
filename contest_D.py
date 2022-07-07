def get_int():
    return int(input())


def get_psw_suggestion(user_psw):
    upper_case = False
    lower_case = False
    vocal = False
    consonant = False
    digit = False

    vocals = {"e", "u", "i", "o", "a", "y", "E", "U", "I", "O", "A", "Y"}
    for ch in user_psw:
        upper_case = upper_case or 65 <= ord(ch) <= 90
        lower_case = lower_case or 97 <= ord(ch) <= 122
        vocal = vocal or ch in vocals

        letter = 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122
        consonant = consonant or (letter and ch not in vocals)
        digit = digit or ch.isdigit()

    good_psw = (upper_case, lower_case, vocal, consonant, digit)
    if all(good_psw):
        return user_psw

    if not upper_case:
        if not vocal:
            user_psw += "A"
            vocal = True
        else:
            user_psw += "D"
            consonant = True
    if not lower_case:
        if not vocal:
            user_psw += "a"
            vocal = True
        else:
            user_psw += "d"
            consonant = True
    if not vocal:
        user_psw += "a"
    if not consonant:
        user_psw += "d"
    if not digit:
        user_psw += "4"

    return user_psw


def main():
    users = get_int()
    for user in range(users):
        user_psw = input()
        print(get_psw_suggestion(user_psw))


if __name__ == '__main__':
    main()
