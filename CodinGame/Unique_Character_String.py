from collections import defaultdict


def isUniqueCharString(str):
    myHashMap = defaultdict(int)
    for i in range(len(str)):
        if str[i] in myHashMap or i >= 256:
            return False
        else:
            myHashMap[str[i]] = 1
    return True


if __name__ == "__main__":
    Name = input(
        "Please, type the string you want to verify its unique characters/n")
    print(isUniqueCharString(Name))
