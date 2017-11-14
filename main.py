import string

aToZ = string.ascii_lowercase

def caesar( input, shift):

    if input.isalpha() is False:
        raise ValueError("Input contains characters not supported (yet)")

    input = input.lower()

    # Adapted from https://stackoverflow.com/a/8895517
    shiftedAToZ = aToZ[shift:] + aToZ[:shift]
    table = str.maketrans( aToZ, shiftedAToZ )

    return input.translate( table )

