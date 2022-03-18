"""
Matplotlib Basics
"""
from os.path import dirname, realpath, join
from matplotlib.pyplot import (
    plot,
    show,
    xlabel,
    ylabel,
    title,
    xlim,
    ylim,
    figure,
    savefig,
)
from numpy import arange


def main():
    """
    main wrapper function
    """
    xarr = arange(0, 10)
    yarr = 2 * xarr
    print(xarr)
    print(yarr)

    figure()
    plot(xarr, yarr)
    xlabel("X Axis Title Here")
    ylabel("Y Axis Title Here")
    title("String Title Here")

    figure()
    plot(xarr, yarr)
    xlabel("X Axis Title Here")
    ylabel("Y Axis Title Here")
    title("String Title Here")
    xlim(0, 6)
    ylim(0, 12)

    figure()
    plot(xarr, yarr)
    savefig(join(dirname(realpath(__file__)), "example.png"))


if __name__ == "__main__":
    main()
    show()
