"""
Matplotlib Sub Plots
"""
from matplotlib.pyplot import show, subplots, tight_layout
from numpy import linspace, arange


def main():
    """
    main wrapper function
    """
    anp = linspace(0, 10, 11)
    bnp = anp**4
    xnp = arange(0, 10)
    ynp = 2 * xnp

    _, axes = subplots()
    axes.plot(xnp, ynp, "r")
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    axes.set_title("title")

    _, axes = subplots(nrows=1, ncols=2)
    print(axes)
    print(axes.shape)

    _, axes = subplots(nrows=2, ncols=2)
    print(axes)
    print(axes.shape)

    _, axes = subplots(nrows=1, ncols=2)
    for axe in axes:
        axe.plot(xnp, ynp)

    _, axes = subplots(nrows=1, ncols=2)
    axes[0].plot(anp, bnp)
    axes[1].plot(xnp, ynp)

    _, axes = subplots(nrows=2, ncols=2)
    axes[0][0].plot(anp, bnp)
    axes[1][1].plot(xnp, ynp)

    _, axes = subplots(nrows=2, ncols=2)
    axes[0][0].plot(anp, bnp)
    axes[1][1].plot(xnp, ynp)
    tight_layout()

    fig, axes = subplots(nrows=2, ncols=2, figsize=(12, 8))
    axes[0][0].plot(anp, bnp)
    axes[0][0].set_title("0 0 Title")
    axes[1][1].plot(xnp, ynp)
    axes[1][1].set_title("1 1 Title")
    axes[1][1].set_xlabel("1 1 X Label")
    axes[0][1].plot(ynp, xnp)
    axes[1][0].plot(bnp, anp)
    fig.suptitle("Figure Level", fontsize=16)

    fig, axes = subplots(nrows=2, ncols=2, figsize=(12, 8))
    axes[0][0].plot(anp, bnp)
    axes[1][1].plot(xnp, ynp)
    axes[0][1].plot(ynp, xnp)
    axes[1][0].plot(bnp, anp)
    fig.subplots_adjust(
        left=None,
        bottom=None,
        right=None,
        top=None,
        wspace=0.9,
        hspace=0.1,
    )

    fig, axes = subplots(nrows=2, ncols=2, figsize=(12, 8))
    axes[0][0].plot(anp, bnp)
    axes[1][1].plot(xnp, ynp)
    axes[0][1].plot(ynp, xnp)
    axes[1][0].plot(bnp, anp)
    fig.savefig("subplots.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
    show()
