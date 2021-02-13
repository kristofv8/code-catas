def sum_str(a, b):
    empty = ""
    if a == empty:
        a = 0
    if b == empty:
        b = 0


    numberone = int(a)
    numbertwo = int(b)

    z = numberone + numbertwo
    y = str(z)

    return y

sum_str("", "2")