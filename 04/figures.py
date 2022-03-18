"""
Matplotlib Figure Object
"""
from os.path import dirname, realpath, join
from matplotlib.pyplot import show, figure
from numpy import linspace, arange


def main():
    """
    main wrapper function
    """
    anp = linspace(0, 10, 11)
    bnp = anp**4
    print(anp)
    print(bnp)
    xnp = arange(0, 10)
    ynp = 2 * xnp
    print(xnp)
    print(ynp)

    fig = figure()
    axes = fig.add_axes([0, 0, 1, 1])
    axes.plot(xnp, ynp)

    fig = figure()
    axes = fig.add_axes([0, 0, 1, 1])
    axes.plot(anp, bnp)
    print(type(fig))

    fig = figure()
    axes1 = fig.add_axes([0, 0, 1, 1])
    axes2 = fig.add_axes([0.2, 0.2, 0.5, 0.5])
    axes1.plot(anp, bnp)
    axes1.set_xlabel("X Label")
    axes1.set_ylabel("Y Label")
    axes1.set_title("Big Figure")
    axes2.plot(anp, bnp)
    axes2.set_title("Small Figure")

    fig = figure()
    axes1 = fig.add_axes([0, 0, 1, 1])
    axes2 = fig.add_axes([0.2, 0.5, 0.25, 0.25])
    axes1.plot(anp, bnp)
    axes1.set_xlabel("X Label")
    axes1.set_ylabel("Y Label")
    axes1.set_title("Big Figure")
    axes2.plot(anp, bnp)
    axes2.set_xlim(8, 10)
    axes2.set_ylim(4000, 10000)
    axes2.set_xlabel("X")
    axes2.set_ylabel("Y")
    axes2.set_title("Zoomed In")


def main2():
    """
    main 2 wrapper function
    """
    anp = linspace(0, 10, 11)
    bnp = anp**4
    xnp = arange(0, 10)
    ynp = 2 * xnp

    fig = figure()
    axes1 = fig.add_axes([0, 0, 1, 1])
    axes2 = fig.add_axes([0.2, 0.5, 0.25, 0.25])
    axes3 = fig.add_axes([1, 1, 0.25, 0.25])
    axes1.plot(anp, bnp)
    axes1.set_xlabel("X Label")
    axes1.set_ylabel("Y Label")
    axes1.set_title("Big Figure")
    axes2.plot(anp, bnp)
    axes2.set_xlim(8, 10)
    axes2.set_ylim(4000, 10000)
    axes2.set_xlabel("X")
    axes2.set_ylabel("Y")
    axes2.set_title("Zoomed In")
    axes3.plot(anp, bnp)

    fig = figure(figsize=(12, 8), dpi=100)
    axes1 = fig.add_axes([0, 0, 1, 1])
    axes1.plot(anp, bnp)

    fig = figure()
    axes1 = fig.add_axes([0, 0, 1, 1])
    axes1.plot(anp, bnp)
    axes1.set_xlabel("X")
    fig.savefig(join(dirname(realpath(__file__)), "figure.png"), bbox_inches="tight")

    fig = figure(figsize=(12, 8))
    axes1 = fig.add_axes([0, 0, 1, 1])
    axes2 = fig.add_axes([1, 1, 0.25, 0.25])
    axes1.plot(xnp, ynp)
    axes2.plot(xnp, ynp)
    fig.savefig(join(dirname(realpath(__file__)), "test.png"), bbox_inches="tight")


if __name__ == "__main__":
    main()
    main2()
    show()
