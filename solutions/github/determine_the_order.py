""" --- Determine the order --- Challenging

The Robots have found an encrypted message. We cannot decrypt
it at the moment, but we can take the first steps towards doing
so. You have a set of "words", all in lower case, and each word
contains symbols in "alphabetical order". (it's not your typical
alphabetical order, but a new and different order.) We need
to determine the order of the symbols from each "word" and create
a single "word" with all of these symbols, placing them in the new
alphabetial order. In some cases, if we cannot determine the order
for several symbols, you should use the traditional latin
alphabetical order. For example: Given words "acb", "bd", "zwa".
As we can see "z" and "w" must be before "a" and "d" after "b".
So the result is "zwacbd".

Input:              Words as a list of strings.
Output:             The order as a string.
How it is used:     This concept can be useful for the cryptology,
                    helping you to find regularities and patterns
                    in natural text and ciphered messages.
Precondition:       For each test, there can be the only one solution.
                    0 < |words| < 10

"""


def my_solution(data):
    def get_letter(words, pool_of_letters, used_letters):
        for l in sorted(pool_of_letters - set(used_letters)):
            if all(next(c for c in w if c not in used_letters) == l for w in words if l in w):
                return l

    letters = set(''.join(data))
    result = ''
    while len(result) < len(letters):
        result += get_letter(data, letters, result)
    return result


def gyahun_dash_solution(strings):
    def topological_sorting(vertices, edges):
        starts = {v for v in vertices if not any(e.endswith(v) for e in edges)}

        if not starts:
            raise StopIteration

        first = min(starts)
        yield first

        passed = {edge for edge in edges if edge.startswith(first)}
        candidates = starts.difference(first) | {edge[1] for edge in passed}
        for i in topological_sorting(candidates, edges - passed):
            yield i

    edges = {p + q for s in strings for p, q in zip(s, s[1:]) if p != q}
    return ''.join(topological_sorting({s[0] for s in strings}, edges))


def sim0000_solution(data):
    alphabet = sorted(set(''.join(data)))
    result = ''
    for n in range(len(alphabet)):
        for c in alphabet:
            if c in result:
                continue
            if all(c not in word or c == word[0] for word in data):
                break
        result += c
        for i in range(len(data)): data[i] = data[i].replace(c, '')
    return result
