def updateBit(n, i, bitIsOne):
    val = 1 if bitIsOne else 0
    mask = ~(1 << i)  # mask = 1111111110111111
    return (n & mask) | val << i
