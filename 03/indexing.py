"""
NumPy Indexing and Selection
"""
from numpy import array, arange


def main():
    """
    main wrapper function
    """
    arr = arange(0, 11)
    print(arr)
    print(arr[8])
    print(arr[1:5])
    print(arr[0:5])
    arr[0:5] = 100
    print(arr)
    arr = arange(0, 11)
    print(arr)
    slice_of_arr = arr[0:6]
    print(slice_of_arr)
    slice_of_arr[:] = 99
    print(slice_of_arr)
    print(arr)
    arr_2d = array(([5, 10, 15], [20, 25, 30], [35, 40, 45]))
    print(arr_2d)
    print(arr_2d[1])
    print(arr_2d[1][0])
    print(arr_2d[1, 0])
    print(arr_2d[:2, 1:])
    print(arr_2d[2])
    print(arr_2d[2, :])
    arr = arange(1, 11)
    print(arr)
    print(arr > 4)
    bool_arr = arr > 4
    print(bool_arr)
    print(arr[bool_arr])
    print(arr[arr > 2])
    xint = 2
    print(arr[arr > xint])


if __name__ == "__main__":
    main()
