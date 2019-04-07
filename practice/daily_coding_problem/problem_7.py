"""

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""
MAPPING = tuple('abcdefghijklmnopqrstuvwxyz')


def count_decodings(code, mapping=MAPPING):
    """
    I overengineered this a bit so it works for essentially any encoding so long as it's represented by numbers starting
    at 1 and ending at the number of different character-codes. There should be no issue with having 2 different codes
    for the same character either. Once the number of different error codes reaches the next order of magnitude,
    it simply becomes possible to have larger codes. In the task, codes could only have values from 1 to 26,
    so either 1 or 2 digits. With 3 digits (so a character code of at least 100), larger substrings of the total code
    have to be considered.

    :param code: code to check, since the code represents an integer, both string and int are handled as input type
    :param mapping: the mapping to use for calculation. default: MAPPING
    :return: number of possible decodings of the code
    """
    code = str(code)
    max_width = max_code_length(mapping)
    counter = [0] * (len(code))
    if is_mapped_code(code[0], mapping):
        counter[0] = 1
    if is_mapped_code(code[:2], mapping):
        counter[1] = 1
    # print(counter)
    # LOOP: time of O(len(code) * log10(max_code_length(mapping)))
    for i in range(len(code)):
        for width in range(1, max_width+1):
            # mind the code[i+1:i+1+width] bit, we're always looking at the section after the current,
            # as the current index is considered 'finished'
            if i+width < len(code) and is_mapped_code(code[i+1:i+1+width], mapping):
                counter[i+width] += counter[i]
        # print(counter)
    return counter[-1]


def is_mapped_code(code, mapping):
    if int(code)-1 < len(mapping):
        return True
    return False


def max_code_length(mapping):
    return int(len(mapping)/10)


def decode_exact(code, mapping):
    num = int(code)
    if is_mapped_code(num, mapping):
        return mapping[num-1]
    raise ValueError("code can not be decoded exactly.")


def encode(message, mapping=MAPPING):
    code = ''
    for c in message:
        if c not in mapping:
            raise ValueError("message not supported")
        code += str(mapping.index(c)+1)
    print(message)
    print(code)
    return code


def main():
    print(count_decodings(encode("aaaa")))
    print(count_decodings(encode("zzzz")))
    print(count_decodings(encode("iiii")))
    print(count_decodings(encode("gabbagandalf")))
    mapping = tuple('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(count_decodings(encode("GabbaGandalfTheGreat", mapping), mapping))
    mapping = tuple('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    print(count_decodings(encode("GabbaGandalfTheGreat", mapping), mapping))


if __name__ == '__main__':
    main()
