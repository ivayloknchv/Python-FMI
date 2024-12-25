from secret import clue


def lucky():
    result = 0

    begin = clue(left_shift=5) >> 5
    result |= begin

    end = clue(right_shift=5) << 5
    result |= end

    mid1 = clue(bw_and=0b00010000) # bitmask with 16
    if mid1 == 0:
        result |= (0<<4)
    else:
        result |= (1<<4)

    mid2 = clue(bw_or=0b11110111) # bitmask with 247
    if mid2 == 0b11111111: # 255
        result |= (1<<3)
    else:
        result |= (0<<3)

    return result
