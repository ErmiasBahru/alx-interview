#!/usr/bin/python3
"""UTF-8 Validation"""

def validUTF8(data):
    """
    Return: True if data is a valid UTF-8 encoding,
    else return False
    """
    for byte in data:
        if byte >> 7 == 0:
            continue
        elif byte >> 5 == 0b110:
            continue
        elif byte >> 4 == 0b1110:
            continue
        elif byte >> 3 == 0b11110:
            continue
        else:
            return False
    return True
