import numpy as np


def main():
    zeros_array = np.chararray((2, 3))
    zeros_array[:] = '.'
    print(zeros_array[1, 2])
    return


if __name__ == '__main__':
    main()
