def calculate_static_margin(cg, cp, diameter):
    """
    Calculate the rocket's static margin in calibers.

    Parameters:
        cg (float): Center of Gravity (m)
        cp (float): Center of Pressure (m)
        diameter (float): Rocket diameter (m)

    Returns:
        float: Static margin in calibers
    """

    return (cp - cg) / diameter