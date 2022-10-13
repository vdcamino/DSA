def isPowerOfTwo(n):
    return n != 0 and ((n - 1) & n == 0)


if __name__ == "__main__":
    res = isPowerOfTwo(-20)
    print(res)
