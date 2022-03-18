"""
Matplotlib Styling
"""
from matplotlib.pyplot import show, figure, subplots
from numpy import arange


def main():
    """
    main wrapper function
    """
    xnp = arange(0, 10)
    fig = figure()
    axes = fig.add_axes([0, 0, 1, 1])
    axes.plot(xnp, xnp**2, label="x**2")
    axes.plot(xnp, xnp**3, label="x**3")
    axes.legend()

    _, axes = subplots()
    axes.plot(xnp, xnp**2, "b.-")
    axes.plot(xnp, xnp**3, "g--")

    _, axes = subplots()
    axes.plot(xnp, xnp + 1, color="blue", alpha=0.5)
    axes.plot(xnp, xnp + 2, color="#8B008B")
    axes.plot(xnp, xnp + 3, color="#FF8C00")

    _, axes = subplots(figsize=(12, 6))
    axes.plot(xnp, xnp - 1, color="red", linewidth=0.25)
    axes.plot(xnp, xnp - 2, color="red", lw=0.50)
    axes.plot(xnp, xnp - 3, color="red", lw=1)
    axes.plot(xnp, xnp - 4, color="red", lw=10)

    _, axes = subplots(figsize=(12, 6))
    axes.plot(xnp, xnp - 1, color="green", lw=3, linestyle="-")
    axes.plot(xnp, xnp - 2, color="green", lw=3, ls="-.")
    axes.plot(xnp, xnp - 3, color="green", lw=3, ls=":")
    axes.plot(xnp, xnp - 4, color="green", lw=3, ls="--")

    _, axes = subplots(figsize=(12, 6))
    lines = axes.plot(xnp, xnp)
    print(type(lines))

    _, axes = subplots(figsize=(12, 6))
    lines = axes.plot(xnp, xnp + 8, color="black", lw=5)
    lines[0].set_dashes([10, 10])

    _, axes = subplots(figsize=(12, 6))
    lines = axes.plot(xnp, xnp + 8, color="black", lw=5)
    lines[0].set_dashes([1, 1, 1, 1, 10, 10])

    _, axes = subplots(figsize=(12, 6))
    axes.plot(xnp, xnp - 1, marker="+", markersize=20)
    axes.plot(xnp, xnp - 2, marker="o", ms=20)
    axes.plot(xnp, xnp - 3, marker="s", ms=20, lw=0)
    axes.plot(xnp, xnp - 4, marker="1", ms=20)

    fig, axes = subplots(figsize=(12, 6))
    axes.plot(
        xnp,
        xnp,
        color="black",
        lw=1,
        ls="-",
        marker="s",
        markersize=20,
        markerfacecolor="red",
        markeredgewidth=8,
        markeredgecolor="blue",
    )


if __name__ == "__main__":
    main()
    show()
