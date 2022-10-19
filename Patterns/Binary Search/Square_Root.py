def findSquareRoot(num, eps):
    l, r = 0, num
    while r - l > eps:
        mid = l + (r - l) / 2
        if mid * mid > num:
            r = mid
        else:
            l = mid
    return mid


if __name__ == "__main__":
    res = findSquareRoot(43.5, 0.0004)
    print(res)
