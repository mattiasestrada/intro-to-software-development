def find_average(array):
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    return sum(array) / len(array)


def gardners_equation(velocity):
    """Calculate the bulk density of the lithology from seismic P-wave velocity using Gardners equation
    Args:
        velocity: Velocity of P-wave in m/s
    Returns:
        density: Bulk density of the lithology in g/cm3
    """
    density = 0.31 * (velocity**0.25)
    return density
