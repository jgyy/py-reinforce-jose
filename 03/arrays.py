"""
Creating NumPy Arrays
"""
from numpy import array, arange, zeros, ones, linspace, eye
from numpy.random import rand, randn, randint


def main():
    """
    main wrapper function
    """
    my_list = [1, 2, 3]
    print(my_list)
    print(array(my_list))

    my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(my_matrix)
    print(array(my_matrix))
    print(arange(0, 10))
    print(arange(0, 11, 2))
    print(zeros(3))
    print(zeros((5, 5)))
    print(ones(3))
    print(ones((3, 3)))
    print(linspace(0, 10, 3))
    print(linspace(0, 5, 20))
    print(linspace(0, 5, 21))
    print(eye(4))
    print(rand(2))
    print(rand(5, 5))
    print(randn(2))
    print(randn(5, 5))
    print(randint(1, 100))
    print(randint(1, 100, 10))
    print(rand(4))

    arr = arange(25)
    ranarr = randint(0, 50, 10)
    print(arr)
    print(ranarr)
    print(arr.reshape(5, 5))
    print(ranarr.max())
    print(ranarr.argmax())
    print(ranarr.min())
    print(ranarr.argmin())
    print(arr.shape)
    print(arr.reshape(1,25))
    print(arr.reshape(1,25).shape)
    print(arr.reshape(25,1))
    print(arr.reshape(25,1).shape)
    print(arr.dtype)

    arr2 = array([1.2, 3.4, 5.6])
    print(arr2.dtype)


if __name__ == "__main__":
    main()
