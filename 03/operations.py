"""
NumPy Operations
"""
from numpy import sqrt, exp, sin, arange, array


def main():
    """
    main wrapper function
    """
    arr = arange(0, 10)
    print(arr)
    print(arr + arr)
    print(arr * arr)
    print(arr - arr)
    print(arr**3)
    print(sqrt(arr))
    print(exp(arr))
    print(sin(arr))
    arr = arange(0, 10)
    print(arr)
    print(arr.sum())
    print(arr.mean())
    print(arr.max())
    arr_2d = array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(arr_2d)
    print(arr_2d.sum(axis=0))
    print(arr_2d.shape)
    print(arr_2d.sum(axis=1))


if __name__ == "__main__":
    main()
