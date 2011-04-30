import random
stdchrs = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def generate_password(length=9, chrs=None):
    """9 length and stdchrs =  13,537,086,546,263,552 permutations
       7 length and stdchrs =       3,521,614,606,208 permutations
       5 length and stdchrs =             916,132,832 permutations
       3 length and stdchrs =                 238,328 permutations"""
    if chrs == None:
        chrs = stdchrs
    return "".join(random.choice(chrs) for x in range(length))
