def reverseBits(n):
    res = 0
    for i in range(32):
        # get the right most bit of the original number
        bit = (
            n >> i
        ) & 1  # AND right most element with 1 to see if it is a zero or a one
        res = res | (
            bit << (31 - i)
        )  # alocate this bit at the current left most position while maintaining the rest intact

    return res


if __name__ == "__main__":
    res = reverseBits(964176192)
    print(res)
