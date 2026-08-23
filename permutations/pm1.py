from itertools import permutations
from math import factorial
from collections import defaultdict


def how_many_permutations(text: str) -> int:
    letters = defaultdict(int)
    for letter in text:
        letters[letter] += 1
    numerator = factorial(len(text))
    factors = [factorial(count) for count in letters.values()]
    denominator = 1
    for factor in factors:
        denominator *= factor
    return numerator // denominator


#perms = {''.join(x) for x in list(permutations("electrocardiographic"))}
#print(perms)
#print(len(perms))

#print(how_many_permutations("electrocardiographic"))
#print(how_many_permutations("disc"))

#print(factorial(9))
