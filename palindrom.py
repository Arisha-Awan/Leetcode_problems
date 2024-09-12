def is_palindrom(x):
    if x < 0:
        return False
    actual = x
    result = 0
    while x:
        mod = x % 10
        result = (result * 10) + mod
        x = x // 10
    return actual == result


def palindrom_str(x):
    x = x.replace(" ", "")
    return x == x[::-1]


def pal_str(x):
    n = len(x)
    for i in range(n // 2):
        if x[i] != x[n - i - 1]:
            return False
    return True


print(pal_str("ABBCBBA"))
# num=int(input("ente a number: "))

# print(is_palindrom(num))
