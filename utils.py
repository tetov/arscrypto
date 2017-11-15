

def letter_from_number(number: int):
    """
    Converts a number to a letter.

    Args:
        number -- Number to convert.
    """

    # if number.isnumeric() is False:
        # raise ValueError("Input is not number.")

    # If number is not in range 0..26 then make it so >:-)
    if not 0 < number <= 26:
        number %= 26

    return A2Z[number-1]
