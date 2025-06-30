def find_average(array):
    return sum(array) / len(array)


def gardners_equation(velocity):
    density = 0.31*(velocity**0.25)
    return density
