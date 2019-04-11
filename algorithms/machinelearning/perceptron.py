"""
training sequence:
[[x0, y0], [x1, y1], ...]

where xi = [xi0, xi1, ...]
"""


def perceptron(training_sequence):
    """
    Perceptron assumes normalised data points!

    :param training_sequence:
    :return:
    """
    weights = [0] * len(training_sequence[0][0])
    while True:
        for x, y in training_sequence:
            if sgn(scalar_product(weights, x) != y):
                weights = add_vectors(weights, [y * val for val in x])
        if all(sgn(scalar_product(weights, x)) == y for x, y in training_sequence):
            break
    return weights


def sgn(x):
    if x < 0:
        return -1
    return 1


def scalar_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must be same length for scalar product")
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


def add_vectors(a, b):
    res = [a[i]+b[i] for i in range(len(a))]
    return res


def normalize_training_sequence(training_sequence):
    _x_list = [x + [1] for x, y in training_sequence]
    _x_norm_list = [euclidean_norm(x) for x in _x_list]
    _x_norm_max = max(_x_norm_list)
    res = []
    for x, y in training_sequence:
        _x = [xi / _x_norm_max for xi in (x + [1])]
        res.append([_x, y])
    return res


def euclidean_norm(x):
    return sqrt(scalar_product(x, x))


def sqrt(x):
    return x**(1/2)


def root(x, n):
    return x**(1/float(n))


def test():
    # TODO:: go through it manually or find an example set to assure everything works as intended
    # TODO:: alternatively, set up a check if all x with y = 1 are 'above' and -1 are 'below' the line
    s = [[[-1, -1], 1], [[-1, 1], 1], [[1, -1], 1], [[1, 1], -1]]
    normalize_training_sequence(s)
    print(perceptron(normalize_training_sequence(s)))


if __name__ == '__main__':
    test()
