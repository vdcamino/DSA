# input = {{Item0,Item1}, {Item2, Item3}, {Item0, Item4}}
# type = string
# return pair with highest length
# if two or more with the same length, return the pair that contains the element with smallest lexological element


def getLexologicalValue(my_pair_of_strings):
    return min(my_pair_of_strings[0], my_pair_of_strings[1])


def pair_highest_number_elem(my_list_of_strings):
    res = list()
    max_pair_size = -1
    max_pair_lexological_val = -1
    for pair in my_list_of_strings:
        curr_pair_length = len(pair[0]) + len(pair[1])
        if curr_pair_length > max_pair_size or (
            curr_pair_length == max_pair_size
            and getLexologicalValue(pair) < max_pair_lexological_val
        ):
            res.insert(0, [pair[0], pair[1]])
            max_pair_lexological_val = getLexologicalValue(pair)
            max_pair_size = curr_pair_length
    return res[0]


if __name__ == "__main__":
    input = [["s", "ss"], ["aaaaaaa", "asd"], ["ss", "ss"]]
    print(pair_highest_number_elem(input))
