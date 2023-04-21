import random

def _randomdata(size, maxvalues=None):
    if maxvalues:
        return [random.randint(0, maxvalues) for _ in range(size)]
    else:
        return [random.randint(0, size) for _ in range(size)]


def shuffled():
    return _randomdata(10 ** 6)

def shuffled_16_values():
    return _randomdata(10 ** 6, 16)

def ascending():
    return [i for i in range(10 ** 6)]

def descending():
    return [10 ** 6 - i for i in range(10 ** 6)]

def pipe_organ():
    return [int(i) for i in range(int(10 ** 6 / 2))] + [int(10 ** 6 / 2 - i) for i in range(int(10 ** 6 / 2))]


""" if __name__ == "__main__":
    # SEE: https://probablydance.com/2017/01/17/faster-sorting-algorithm-part-2/

    with open('./testdatas/shuffled_1M.csv', 'w') as fp:
        for item in shuffled:
            fp.write(f'{item}\n')

    with open('./testdatas/shuffled_1M_16val.csv', 'w') as fp:
        for item in shuffled_16_values:
            fp.write(f'{item}\n')

    with open('./testdatas/asc.csv', 'w') as fp:
        for item in ascending:
            fp.write(f'{item}\n')

    with open('./testdatas/dsc.csv', 'w') as fp:
        for item in descending:
            fp.write(f'{item}\n')

    with open('./testdatas/pipeorgan.csv', 'w') as fp:
        for item in pipe_organ:
            fp.write(f'{item}\n')
 """

