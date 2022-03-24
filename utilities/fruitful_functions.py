"""
Created on Feb 19, 2019

@author: toni
"""

import bisect as bs
import math
import random as rn
import time

import structshape as ss


def matrix_multiplication(A, B):
    """Multiply two matrices in list form."""
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
        print("Cannot multiply the two matrices. Incorrect dimensions.")
        return None

    # create the result matrix with dimensions rows_A x cols_B
    C = [[0 for col in range(cols_B)] for row in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B, it's the same
                C[i][j] += A[i][k] * B[k][j]

    return C


def is_between(x, y, z):
    """Check whether or not the argument y is between x and z."""
    if x < y < z:
        return True
    return False


def ack(m, n):
    """Evaluate Ackermann's function and returns its value.
    http://en.wikipedia.org/wiki/Ackermann_function
    """
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


def ack_memo(m, n):
    """
    Evaluate Ackermann's function and return its value while using the memos.
    http://en.wikipedia.org/wiki/Ackermann_function
    """
    cache = {}
    if m == 0:
        return n + 1
    if n == 0:
        return ack_memo(m - 1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ack_memo(m - 1, ack_memo(m, n - 1))
        return cache[m, n]


def first(word):
    """Return the first character of a string."""
    return word[0]


def last(word):
    """Return the last character of a string."""
    return word[-1]


def middle(word):
    """Return all but the first and last characters of a string."""
    return word[1:-1]


def is_palindrome(word):
    """Return True if word is a palindrome."""
    if len(word) <= 1:
        return True

    if first(word) != last(word):
        return False

    return is_palindrome(middle(word))


def is_palindrome_(word):
    """Check whether a word is a palindrome or not."""
    return word == word[::-1]


def is_power(a, b):
    """Check whether or not a is a power of b."""
    if a % b == 0:
        is_power(a / b, b)
        return True
    return False


def gcd(a, b):
    """Determine the greatest common divisor of two numbers a and b."""
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


def square_root(a):
    """Estimate the square root of a."""
    epsilon = 0.00000001  # tolerance
    x = 1  # initial guess

    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            break
        x = y
    return y


def test_square_root():
    """Compare math.sqrt(i) and square_root(i)."""
    for i in range(10):
        e = square_root(i + 1)
        m = math.sqrt(i + 1)
        r = abs(e - m)
        print(f'{i + 1:2d} {e:.15f} {m:.15f} {r:.18f}')


def eval_loop():
    """Prompt the user for an input, evaluate it and print the evaluation.
    Break if the input is 'done' and return the last evaluated expression.
    """
    res = None

    while True:
        inp = input('> ')
        if inp == 'done':
            return res
        res = eval(inp)
        print(res)


def factorial(n):
    """Return the factorial of n."""
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    if n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    if n == 0:
        return 1
    return n * factorial(n - 1)


def estimate_pi():
    """Return the estimate of pi according to Srinivasa."""
    k = 0
    suminf = 0

    while True:
        facn = factorial(4 * k)
        facd = factorial(k)
        n = facn * (1103 + 26390 * k)
        d = facd ** 4 * 396 ** (4 * k)
        summand = n / d
        suminf += summand
        if summand < 1e-15:
            break
        k += 1

    c = 2 * math.sqrt(2) / 9801
    estpi = 1 / (c * suminf)
    mathpi = math.pi
    print(estpi, mathpi, abs(estpi - mathpi))


def any_lowercase1(s):
    """Incorrect because the function terminates after the first element.
    The return has to be outside the loop."""
    for c in s:
        if c.islower():
            return True
        return False


def any_lowercase2(s):
    """Return breaks the loop, and the string 'c' as a condition is always
    true no matter the input."""
    for c in s:
        if 'c'.islower():
            return 'True'
        return 'False'


def any_lowercase3(s):
    """This only checks the last element."""
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Always returns true for the last element because of the logical
    operator or."""
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    """Check if there are any uppercase letters in a string and return
    false if there are. Return true if there are only lowercase letters."""
    for c in s:
        if not c.islower():
            return False
    return True


def rotate_letter(letter, n):
    """Rotate a letter by n places. Does not change other chars.

    letter -- single-letter string
    n -- int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(s, n):
    """A method of encryption which rotates the word s by n."""
    rword = ''
    for letter in s:
        rword += rotate_letter(letter, n)
    return rword


def avoids(s, f):
    """Check whether or not the string s contains the characters of the
    string f."""
    for item in s:
        if item in f:
            return False
    return True


def uses_only(s, f):
    """Return True if the string s contains only the letters of string f."""
    for item in s:
        if item not in f:
            return False
    return True


def uses_all(s, r):
    """Return True if the string s contains all the letters of string r
    at least once."""
    for char in r:
        if char not in s:
            return False
    return True


def nested_sum(lis):
    """Return a sum of every element from a nested list."""
    total = 0
    for item in lis:
        # duck type, i.e. avoid checking the object type
        try:
            total += item
        except TypeError:
            total += nested_sum(item)
    return total


def capitalize_all(t):
    """Return a mapped list res from list t."""
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


def capitalize_nested(a):
    """Return a mapped nested list res from a nested list t."""
    res = []
    for s in a:
        try:
            res.append(s.capitalize())
        except AttributeError:
            res.append(capitalize_nested(s))
    return res


def cumulative_list(a):
    """Return a cumulative list from an integer list a."""
    cummlist = []
    for index_ in range(len(a)):
        cummlist.append(sum(a[:index_ + 1]))
    return cummlist


def middle_list(a):
    """Take a list a, remove the first and last element of a and return the
    updated list.
    """
    return a[1:-1]


def chop(a):
    """Remove the first and last element from list a and return None."""
    if len(a) <= 2:
        a = []
    else:
        del a[0], a[-1]
    return None


def is_sorted(t):
    """Check whether the elements of a list t are sequenced in an ascending
    order.
    """
    dummy = t[:]
    dummy.sort()
    return t == dummy


def is_anagram(t, u):
    """Take two strings t and u and check whether u is an anagram of t."""
    tl = list(t)
    ul = list(u)
    tl.sort()
    ul.sort()
    return tl == ul


def str_to_list(s):
    """Take a string s and add its letters to a list."""
    return list(s)


def has_duplicates(z):
    """Check whether the list z contains any duplicate elements and return
    True if it does, False otherwise."""
    for index_ in range(len(z) - 1):
        if z[index_] in z[index_ + 1:]:
            return True
    return False


def dict_duplicates(d):
    """Version of has_duplicates which checks for duplicates in a dictionary.
    """
    i = invert_dict(d)
    for key in i:
        if len(i[key]) > 1:
            return True
    return False


def has_duplicates2(t):
    """Check whether any element appears more than once in a sequence.

    t -- sequence
    """
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates3(t):
    """More efficient version using sets."""
    return len(set(t)) < len(t)


def rand_birthday(n):
    """Return a list of integers between 1 and 365, with length (n)."""
    t = []
    for _ in range(n):
        bday = rn.randint(1, 365)
        t.append(bday)
    return t


def remove_duplicates(d):
    """Remove duplicate elements from the list d.

    O(n^2) problem, useful for small lists, but very slow for large lists.
    If order is not important, the solution is return list(set(d))"""
    t = []
    for i in d:
        if i not in t:
            t.append(i)
    return (t, len(t))


def f7(seq):
    """Take a sequence seq and return a new sequence in the same order with
    duplicates removed."""
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def index(a, x):
    """Locate the leftmost value exactly equal to x.

    The bisection algorithm for searching the word in a sorted word list."""
    i = bs.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None


def sum_all(*args):
    """Take a variable number of arguments and return their sum."""
    result = 0
    for item in args:
        result += item
    return result


def sort_by_length(words):
    """Sort the words by length."""
    t = []
    for word in words:
        t.append((len(word), word))
        t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res


def sort_by_length_random(words):
    """Sort the words by length.

    Sorting criteria in order: length of the word, a random number,
    alphabetical order of words."""
    t = []
    for word in words:
        t.append((len(word), rn.random(), word))
        t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res


def most_frequent(s):
    """Return the letters of a string in a decreasing order of frequency."""
    t = []
    for key, val in histogram_with_get(s).items():
        t.append((val, key))
    t.sort(reverse=True)  # the alphabetical order won't be preserved

    res = []
    for freq, letter in t:
        res.append(letter)
    return res


def duration(a):
    """Call a function, measure its execution time and return that time."""
    start = time.time()
    a
    end = time.time()
    return end - start


def timings(b, n=12):
    """Measure execution times of a python function.

    b -- python function
    n -- number of tests
    """
    for _ in range(n):
        yield duration(b)


def average_time(c):
    """Return average execution time of a python function.

    c -- generator object"""
    tmp = tuple(c)  # create an intermediate variable, exhaust the generator
    return sum(tmp) / len(tmp)


def execution_time(funobj, funinp):
    """Return the execution time of a python function."""
    # return average_time(timings(funobj))
    print(f"Average execution time of {funobj.__name__}: "
          f"{average_time(timings(funobj(funinp)))}")


def histogram(s):
    """In statistics, a histogram is a set of counters (or frequencies).

    s -- string
    returns: dict"""
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def histogram_with_get(s):
    """
    s -- string
    returns: dict
    """
    d = dict()
    for c in s:
        # every time a key repeats we get its value and increase it by 1
        d[c] = d.get(c, 0) + 1
    return d


def print_hist(h):
    """Take a dict h and print its keys and values in alphabetical order."""
    k = list(h.keys())
    k.sort()
    for index_, c in enumerate(h):
        print(k[index_], h[c])


def reverse_lookup(d, v):
    """Search the dictionary d for value v and return a list of all keys
    that point to value v. If there is no value v in the dictionary,
    reverse_lookup returns an empty list."""
    keys = []
    for k in d:
        if d[k] == v:
            keys.append(k)
    return keys


def invert_dict(d):
    """Take a dictionary, and invert its keys and values. If there are more
    keys that have the same value, the key from that value points to a list
    of the former keys."""
    inverse = dict()
    for key, val in d.items():
        inverse.setdefault(val, []).append(key)
    return inverse


def fibonacci_memo(n):
    """A dictionary stores known values and they don't have to be computed
    again."""
    known = {0: 0, 1: 1}
    if n in known:
        return known[n]
    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def signature(s):
    """Return the signature of a string. A signature is a string that contains
    all letters of the input string in order.
    """
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Find all anagrams in a list of words.

    filename -- string, filename of the word list

    returns: a map from each word to a list of its anagrams
    """
    d = {}
    for line in open(filename, encoding='utf-8'):
        word = line.strip().lower()
        t = signature(word)

        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def filter_length(d, n):
    """Select only the words in d that have n letters.

    d -- map from a word to list of its anagrams
    n -- integer, number of letters

    returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.iteritems():
        if len(word) == n:
            res[word] = anagrams
    return res


def difference(s1, s2):
    """Find the difference of two strings of the same length."""
    count = 0
    for index_ in range(len(s1)):
        if s1[index_] != s2[index_]:
            count += 1
    return count


def main():
    print(duration(ack(3, 6)))

    print(is_palindrome('word'))
    print(is_palindrome('nakamura'))
    print(is_palindrome('alala'))
    print(is_palindrome('ab'))
    print(is_palindrome('tt'))

    print(is_power(8, 2))
    print(is_power(81, 3))
    print(is_power(256, 4))
    print(is_power(45, 6))

    print(gcd(2, 3))
    print(gcd(234, 14))
    print(gcd(156, 24))
    print(gcd(3564, 4857))

    print(square_root(7))
    test_square_root()
    estimate_pi()

    s = 'banana'
    print(s.count('a'))

    print(is_palindrome_('Hello'))

    print(any_lowercase1('string'))
    print(any_lowercase2('String'))
    print(any_lowercase3('string'))
    print(any_lowercase4('string'))
    print(any_lowercase5('string'))

    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('idiot', 13))

    b = [2, 6, 3, 34, 26, 15, [3, 5, 89, 4]]
    g = [[64, 45, 45], 4, [35, 6, 654, 345], 54, [348, 6]]
    print(nested_sum(b))
    print(nested_sum(g))

    r = ['erh', 're', 'trth']
    print(capitalize_all(r))
    r = ['re', 'trth', ['erh', 'fjdk', 'fd'], 'hei']
    print(capitalize_nested(r))

    b = [1, 5, 3, 6, 3, 5]
    print(cumulative_list(b))

    k = [3, 5, 3, 5, 4, 5, 1, 6]
    print(middle_list(k))

    print(is_anagram('boa', 'oab'))
    print(is_anagram('lenel', 'enlll'))
    print(is_anagram('lenel', 'enlllh'))

    print(has_duplicates(['f', 'g', 'g', 't']))
    print(has_duplicates([3, 5, 2, 1]))

    h = histogram('responsibility')
    print(h)
    print(histogram_with_get('responsibility'))
    keys = reverse_lookup(h, 2)
    print(keys)
    invert = invert_dict(h)
    print(invert)

    print(duration(fibonacci_memo(29)))
    print(duration(fibonacci(29)))

    print(most_frequent('imposibility'))

    a = [[1, 2], [3, 4]]
    b = [[1, 2, 3], [4, 5, 6]]
    print(matrix_multiplication(a, b))


if __name__ == "__main__":
    main()
