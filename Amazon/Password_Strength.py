# Find the password strength.
# For each substring of the password which contains at least one vowel and one consonant, its strength goes up by 1.
# vowels={'a', 'e', 'i', 'o', 'u'}, and rest of letters are all consonant.
# (Only lower alphabet letters)

# Input:
# thisisbeautiful
# output:
# 6
# explaination:
# this, is, be, aut, if, ul

# input:
# hackerrank
# output:
# 3
# explaination:
# hack, er, rank

# input:
# aeiou
# output:
# 0


def password_strength(passwrd):
    vowels = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
    count = 0
    currString = ""
    mySubstrings = []
    consonants_in_substring, vowels_in_substring = 0, 0
    for letter in passwrd:
        currString += letter
        if letter in vowels:
            vowels_in_substring += 1
        else:
            consonants_in_substring += 1
        if consonants_in_substring >= 1 and vowels_in_substring >= 1:
            mySubstrings.append(currString)
            currString = ""
            count += 1
            consonants_in_substring, vowels_in_substring = 0, 0
    return count, mySubstrings


def main():
    input = "thisisbeautiful"
    ans, listss = password_strength(input)
    print(ans, listss)


if __name__ == "__main__":
    main()
