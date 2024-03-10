#!/usr/bin/python3

def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Iterate through each integer in the data
    for num in data:
        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Determine the number of bytes for this character
            if num >> 5 == 0b110:
                num_bytes = 1
            elif num >> 4 == 0b1110:
                num_bytes = 2
            elif num >> 3 == 0b11110:
                num_bytes = 3
            elif num >> 7 == 0:
                num_bytes = 0
            else:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If we finished iterating and all bytes are consumed, it's valid
    return num_bytes == 0
