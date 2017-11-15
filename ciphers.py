""" Collection of cipher decrypting functions. """

import string

A2Z = string.ascii_lowercase

def caesar(encrypted_msg, shift: int):
    """
    Decrypt string using the Caesar cipher

    Args:
        encrypted_msg -- String to decrypt.
        shift -- Amount to shift alphabet by.

    TODO: Add more alphabet's.
    """

    if encrypted_msg.isalpha() is False:
        raise ValueError("Input contains characters not supported (yet)")

    encrypted_msg = encrypted_msg.lower()

    # Adapted from https://stackoverflow.com/a/8895517
    shifted_a2z = A2Z[shift:] + A2Z[:shift]
    table = str.maketrans(A2Z, shifted_a2z)

    return encrypted_msg.translate(table)

def atbash(encrypted_msg):
    """
    Decrypts ATBASH encrypted text.
    """

def vinegere(msg, key, direction):
    """
    Encrypts or decrypts the Vigenère cipher.

    Args:
        msg -- String to encrypt or decrypt.
        key -- String used as key for cipher.
        direction -- Switch to change between encryption or decryption.
    """