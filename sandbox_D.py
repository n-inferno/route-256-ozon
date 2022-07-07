user_logins = set()


def validate(login):
    if login.startswith("-"):
        return False
    if len(login) < 2 or len(login) > 24:
        return False
    lower_login = login.lower()
    if lower_login in user_logins:
        return False
    for ch in login:
        if ch in {"_", "-"}:
            continue
        if ch.isdigit() or (65 <= ord(ch) <= 90) or (97 <= ord(ch) <= 122):
            continue
        return False

    user_logins.add(lower_login)
    return True


if __name__ == '__main__':
    num = int(input())
    for _ in range(num):
        registrations = int(input())
        for reg in range(registrations):
            login = input()
            print("YES" if validate(login) else "NO")
        user_logins.clear()
        print()
