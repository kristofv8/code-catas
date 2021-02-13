def positive_sum(dodawanie):
    suma = 0
    for pierwszy in dodawanie:
        if pierwszy > 0:
            suma += pierwszy

    return suma

positive_sum([1])
