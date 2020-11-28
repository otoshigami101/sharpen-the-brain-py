def run(start, end):
    """
    fibonacci count
    """

    a = []
    b = 0
    c = 0

    while 1:
        c = start if c == 0 else c + 1

        if (len(a) == 2):
            c = a[0] + a[1]

            a[0] = c  # result
            a[1] = a[1] if b == 0 else b  # result before

            b = c  # set to result
        else:
            a.append(c)

        if c > end:
            print str(c) + " is more than " + str(end) + ", bye.."
            break

        print c


def set():
    ''
    try:
        start = int(raw_input("start >"))
        end = int(raw_input("end after num is bigger than >"))

    except ValueError:
        print "\nValue must be number\n"
        return set()

    return start, end


if __name__ == "__main__":
    start, end = set()

    run(start, end)
