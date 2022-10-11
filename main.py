from distutils.log import ERROR


class ERROR(Exception):
    pass


class Solver:
    alphabet = ('a', 'b', 'c', '1')
    operations = ('.', '+', '*')

    def check_sizes(threshold, *lists):
        for lst in lists:
            if len(lst) < threshold:
                return False
        return True

    def handle_concatenation(max_word_len: list, max_suffix_len: list):
        if not Solver.check_sizes(2, max_word_len, max_suffix_len):
            raise ERROR

        max_word_last = max_word_len.pop()
        max_word_prev = max_word_len.pop()

        max_suffix_last = max_suffix_len.pop()
        max_suffix_prev = max_suffix_len.pop()

        if max_word_last is not None and max_word_prev is not None:
            max_word_len.append(max_word_last + max_word_prev)
        else:
            max_word_len.append(None)

        if max_word_last is not None:
            max_suffix_len.append(max(max_suffix_prev + max_word_last, max_suffix_last))
        else:
            max_suffix_len.append(max_suffix_last)

    def handle_union(max_word_len, max_suffix_len):
        if not Solver.check_sizes(2, max_word_len, max_suffix_len):
            raise ERROR

        max_word_last = max_word_len.pop()
        max_word_prev = max_word_len.pop()

        max_suffix_last = max_suffix_len.pop()
        max_suffix_prev = max_suffix_len.pop()

        if max_word_last is None and max_word_prev is None:
            max_word_len.append(None)
        else:
            if (max_word_prev is None):
                max_word_len.append(max_word_last)
            elif (max_word_last is None):
                max_word_len.append(max_word_prev)
            else:
                max_word_len.append(max(max_word_last, max_word_prev))

        max_suffix_len.append(max(max_suffix_prev, max_suffix_last))

    def handle_kleene_star(max_word_len, max_suffix_len):
        if not Solver.check_sizes(1, max_word_len, max_suffix_len):
            raise ERROR

        max_word_last = max_word_len.pop()
        max_suffix_last = max_suffix_len.pop()

        if max_word_last is None or max_word_last == 0:
            max_word_len.append(0)
            max_suffix_len.append(max_suffix_last)
        else:
            max_word_len.append(float('inf'))
            max_suffix_len.append(float('inf'))

    def handle_required_letter(max_word_len, max_suffix_len):
        max_word_len.append(1)
        max_suffix_len.append(1)

    def handle_empty_letter(max_word_len, max_suffix_len):
        max_word_len.append(0)
        max_suffix_len.append(0)

    def handle_letter(max_word_len, max_suffix_len):
        max_word_len.append(None)
        max_suffix_len.append(0)

    def has_suffix(regular_expression, letter, letter_degree):
        max_word_len = []
        max_suffix_len = []

        for symbol in regular_expression:
            if symbol == letter:
                Solver.handle_required_letter(max_word_len, max_suffix_len)
            elif symbol == '1':
                Solver.handle_empty_letter(max_word_len, max_suffix_len)
            elif symbol in Solver.alphabet:
                Solver.handle_letter(max_word_len, max_suffix_len)
            elif symbol == '.':
                Solver.handle_concatenation(max_word_len, max_suffix_len)
            elif symbol == '+':
                Solver.handle_union(max_word_len, max_suffix_len)
            elif symbol == '*':
                Solver.handle_kleene_star(max_word_len, max_suffix_len)
            else:
                raise ERROR


        if len(max_word_len) != 1 or len(max_suffix_len) != 1:
            raise ERROR


        return max_suffix_len[0] >= letter_degree


if __name__ == '__main__':
    delta, x, k = input().split()
    k = int(k)
    if (Solver.has_suffix(delta, x, k)):
        print('YES')
    else:
        print('NO')
