"""
Collection of cipher decrypting functions.

    TODO: Add more alphabet's.
"""
import string
import re

A2Z = string.ascii_lowercase

def caesar(msg, shift: int):
    """
    Decrypt string using the Caesar cipher

    Args:
        msg -- String to decrypt.
        shift -- Amount to shift alphabet by.

    Tests:
        >>> caesar('bzdrzq', 1)
        'caesar'
        >>> caesar('wcjbyl', -20)
        'cipher'
        >>> caesar('åäö', 5)
        Traceback (most recent call last):
            ...
        ValueError: Input contains letters not part of selected alphabet
        >>> caesar('~non-alpha!', 5)
        Traceback (most recent call last):
            ...
        ValueError: Input contains non-alphabetic characters
        >>> caesar('pvupgsbohf', -1247)
        'outofrange'
    """

    msg = msg.lower()

    if msg.isalpha() is False:
        raise ValueError("Input contains non-alphabetic characters")

    if re.findall(r'[^.a-z]', msg):
        raise ValueError("Input contains letters not part of selected alphabet")

    # If shift is more than length of alphabet then make it not so >:-)
    if shift > len(A2Z):
        shift %= len(A2Z)

    if shift < -len(A2Z):
        shift = len(A2Z) - shift % (len(A2Z))

    # Adapted from https://stackoverflow.com/a/8895517
    shifted_a2z = A2Z[shift:] + A2Z[:shift]
    table = str.maketrans(A2Z, shifted_a2z)

    return msg.translate(table)

def atbash(msg):
    """
    Decrypts ATBASH encrypted text.

    Args:
        msg -- String encrypt or decrypt.

    Tests:
        >>> atbash('zgyzhs')
        atbash
        >>> atbash('XZKGRZOH')
        capitals
        >>> atbash('åäö')
        Traceback (most recent call last):
            ...
        ValueError: Input contains letters not part of selected alphabet
        >>> atbash('~non-alpha!')
        Traceback (most recent call last):
            ...
        ValueError: Input contains non-alphabetic characters
    """

    msg = msg.lower()

    if msg.isalpha() is False:
        raise ValueError("Input contains non-alphabetic characters")

    if re.findall(r'[^.a-z]', msg):
        raise ValueError("Input contains letters not part of selected alphabet")

    # Reverse string solution from https://stackoverflow.com/a/27843760
    reversed_a2z = A2Z[::-1]
    table = str.maketrans(A2Z, reversed_a2z)

    return msg.translate(table)

def vinegere(msg, key, direction):
    """
    Encrypts or decrypts the Vigenère cipher.

    Args:
        msg -- String to encrypt or decrypt.
        key -- String used as key for cipher.
        direction -- Switch to change between encryption or decryption.
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
