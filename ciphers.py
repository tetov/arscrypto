"""
Collection of cipher decrypting functions.

    TODO: Add more alphabet's.
    TODO: Support upper case.
"""

import string
import re

A2Z = string.ascii_lowercase

def caesar(msg, shift: int, alphabet=A2Z):
    """
    Decrypt string using the Caesar cipher

    Args:
        msg -- String to decrypt.
        shift -- Amount to shift alphabet by.

    Tests:
        >>> caesar('bzdrzq', 1)
        'caesar'
        >>> caesar('wCjbyl', -20)
        'cipher'
        >>> caesar('pvuPgsbohf', -1247)
        'outofrange'
    """

    msg = sanitize_string(msg)

    # If shift is more than length of alphabet then make it not so >:-)
    if shift > len(alphabet):
        shift %= len(alphabet)

    if shift < -len(alphabet):
        shift = len(alphabet) - shift % (len(alphabet))

    # Adapted from https://stackoverflow.com/a/8895517
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)

    return msg.translate(table)

def atbash(msg, alphabet=A2Z):
    """
    Encrypts or decrypts strings using the Atbash cipher.

    Args:
        msg -- String encrypt or decrypt.

    Tests:
        >>> atbash('zgyzhs')
        'atbash'
        >>> atbash('XZKRGZOH')
        'capitals'
    """

    msg = sanitize_string(msg)

    # Reverse string solution from https://stackoverflow.com/a/27843760
    reversed_alphabet = alphabet[::-1]
    table = str.maketrans(alphabet, reversed_alphabet)

    return msg.translate(table)

def vigenere(msg, key, direction=1, alphabet=A2Z):
    """
    Encrypts or decrypts the Vigenère cipher.

    Args:
        msg -- String to encrypt or decrypt.
        key -- String used as key for cipher.
        direction:
            0 -- decrypt
            1 -- encrypt
        alphabet -- Alphabet to use.
    """
    from itertools import cycle

    msg = sanitize_string(msg)
    key = sanitize_string(key)

    print(msg)
    print(key)
    print(direction)
    print(alphabet)

    # From https://stackoverflow.com/a/21497240
    # I need to figure out how to run this, does it go in its own function?
    for i, j in zip(msg, cycle(key)):
        index = alphabet.index(i) + alphabet.index(j)
        print(alphabet[index % len(alphabet)])



def letter_from_number(number: int, alphabet=A2Z):
    """
    Converts a number to a letter.

    Args:
        number -- Number to convert.
    """

    # If number is not in range 0..26 then make it so >:-)
    if number > len(alphabet):
        number %= len(alphabet)

    return alphabet[number-1]

def number_from_letter(msg, alphabet=A2Z):
    """
    Converts a letter to a number

    Args:
        msg -- Letters to convert.
    """

    msg = sanitize_string(msg)

    return ord(msg) - 96

def sanitize_string(msg):
    '''
    Sanitizes input strings

    Args:
        msg -- String to check.

    Tests:
        >>> atbash('~non-alpha!')
        Traceback (most recent call last):
            ...
        ValueError: Input contains non-alphabetic characters
        >>> sanitize_string('åäö')
        Traceback (most recent call last):
            ...
        ValueError: Input contains letters not part of selected alphabet
    '''

    msg = msg.lower()

    if msg.isalpha() is False:
        raise ValueError("Input contains non-alphabetic characters")

    if re.findall(r'[^.a-z]', msg):
        raise ValueError("Input contains letters not part of selected alphabet")

    return msg

if __name__ == "__main__":
    import doctest
    doctest.testmod()
