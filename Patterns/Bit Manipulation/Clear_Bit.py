def clearBit(n, i):
    mask = ~(1 << i)
    # mask = 111111110111111
    return n & mask
