from fractions import Fraction


def iteration(matrix, x_i, accuracy, steps):
    new_x = []
    for i, var in enumerate(matrix):
        new_x.append(var[-1])
        for j, v in enumerate(var[:-1]):
            if j != i:
                new_x[i] += v * x_i[j]
        new_x[i] /= matrix[i][i]
    steps.append(new_x)
    if max([abs(new_x[i] - x_i[i]) for i in range(len(x_i))]) <= accuracy:
        return new_x
    else:
        return iteration(matrix, new_x, accuracy, steps)


def jacobi(matrix, accuracy=0.0001):
    x = []
    steps = []
    for i, var in enumerate(matrix):
        sum_ = 0
        for j, v in enumerate(var[:-1]):
            if j != i:
                sum_ += abs(v)
        if abs(matrix[i][i]) < sum_:
            return None, None
        x.append(Fraction(var[-1] / var[i]))
    x = iteration(matrix, x, accuracy, steps)
    return x, steps
