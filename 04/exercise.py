"""
Matplotlib Exercises
"""
from matplotlib.pyplot import (
    show,
    figure,
    plot,
    title,
    xlabel,
    ylabel,
    xlim,
    yscale,
    grid,
    legend,
    subplots,
    yticks,
)
from numpy import linspace

labels = [
    "1 Mo",
    "3 Mo",
    "6 Mo",
    "1 Yr",
    "2 Yr",
    "3 Yr",
    "5 Yr",
    "7 Yr",
    "10 Yr",
    "20 Yr",
    "30 Yr",
]
july16_2007 = [4.75, 4.98, 5.08, 5.01, 4.89, 4.89, 4.95, 4.99, 5.05, 5.21, 5.14]
july16_2020 = [0.12, 0.11, 0.13, 0.14, 0.16, 0.17, 0.28, 0.46, 0.62, 1.09, 1.31]


def main():
    """
    main wrapper function
    """
    mass = linspace(0, 10, 11)
    print(f"The array m should look like this: \n\n{mass}")
    clight = 3 * 10**8
    energy = mass * clight**2
    print(f"The array E should look like this: \n\n {energy}")

    figure()
    plot(mass, energy, color="red", lw=5)
    title("E=mc^2")
    xlabel("Mass in Grams")
    ylabel("Energy in Joules")
    xlim(0, 10)

    figure()
    plot(mass, energy, color="red", lw=5)
    title("E=mc^2")
    xlabel("Mass in Grams")
    ylabel("Energy in Joules")
    xlim(0, 10)
    yscale("log")
    grid(which="both", axis="y")

    fig = figure()
    axes = fig.add_axes([0, 0, 1, 1])
    axes.plot(labels, july16_2007, label="july16_2007")
    axes.plot(labels, july16_2020, label="july16_2020")
    legend()

    fig = figure()
    axes = fig.add_axes([0, 0, 1, 1])
    axes.plot(labels, july16_2007, label="july16_2007")
    axes.plot(labels, july16_2020, label="july16_2020")
    legend(loc=(1.04, 0.5))

    fig, axes = subplots(nrows=2, ncols=1, figsize=(12, 8))
    axes[0].plot(labels, july16_2007, label="july16_2007")
    axes[0].set_title("July 16th, 2007")
    axes[1].plot(labels, july16_2020, label="july16_2020")
    axes[1].set_title("July 16th, 2020")

    fig, ax1 = subplots(figsize=(12, 8))
    ax1.plot(labels, july16_2007, lw=2, color="blue")
    ax1.set_ylabel("2007", fontsize=18, color="blue")
    ax1.spines["left"].set_color("blue")
    ax1.spines["left"].set_linewidth(4)
    for label in ax1.get_yticklabels():
        label.set_color("blue")
    yticks(fontsize=15)
    ax2 = ax1.twinx()
    ax2.plot(labels, july16_2020, lw=2, color="red")
    ax2.set_ylabel("2020", fontsize=18, color="red")
    ax2.spines["right"].set_color("red")
    ax2.spines["right"].set_linewidth(4)
    for label in ax2.get_yticklabels():
        label.set_color("red")
    ax1.set_title("July 16th Yield Curves")
    yticks(fontsize=15)


if __name__ == "__main__":
    main()
    show()
