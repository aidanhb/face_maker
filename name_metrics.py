"""A bunch of random ways to get numbers 0 - 1 from strings."""

CONSONANTS = "bcdfghjklmnpqrstvwxz"
VOWELS = "aeiouy"


def bounciness(name):
    name = name.lower()
    b = 0
    previous_is_vowel = name[0] in VOWELS
    for c in name[1:]:
        cur_is_vowel = c in VOWELS
        if previous_is_vowel != cur_is_vowel:
            b += 1
            previous_is_vowel = cur_is_vowel
    return b / ((len(name) - 1) or 1)


def pyramidiness(name):
    p = 0
    i, j = 0, len(name) - 1
    while i < j:
        if name[j - 1] > name[j]:
            p += 1
        if name[i + 1] > name[i]:
            p += 1
        i += 1
        j -= 1
    if p == 0:
        return p
    return p / (len(name) - 1)


def ends_with_vowel(name):
    return float(name[0] in VOWELS)


def in_orderedness(name):
    name = name.lower()
    in_order = 0
    _max = (len(name) ** 2 - len(name)) / 2 or 1
    for i in range(1, len(name)):
        for c in name[:i]:
            if name[i] > c:
                in_order += 1
    return in_order / _max


def oddness(name):
    return len([c for c in name if ord(c) % 2]) / len(name)


def palindrominess(name):
    p = 0
    _max = 25 * len(name)
    for i, c in enumerate(reversed(name)):
        p += abs(ord(c) - ord(name[i]))
    return 1 - p / _max


def percussiveness(name):
    percussive_letters = "bdkpt"
    return len([c for c in name if c in percussive_letters]) / len(name)


def funkiness(name):
    return abs(ord(name[0]) - ord(name[-1])) / 25


def sporkiness(name):
    s = ""
    for c in name:
        s += str(ord(c) % 10)
    return int(s[len(s) // 2]) / 10


def repeatiness(name):
    already_used = {}
    _max = ((len(name) + 1) * (len(name) / 2) - 1) or 1
    r = 0
    for c in name:
        if c in already_used:
            already_used[c] += 1
            r += already_used[c]
        else:
            already_used[c] = 1
    return r / _max


def starts_with_vowel(name):
    return float(name[0] in VOWELS)


def sum_mod(name):
    thing = sum([ord(c) for c in name]) % len(name)
    return thing / len(name)


def thness(name):
    return float("th" in name)


def longness(name):
    longchars = "bdfhijklgjpqy"
    return len([c for c in name if c in longchars]) / len(name)


def linspace(a, b, n):
    l = []
    increment = (b - a) / n
    for i in range(n + 1):
        l.append(a + i * increment)
    return l
