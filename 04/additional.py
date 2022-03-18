"""
Matplotlib Advanced Object
"""
from matplotlib import rcParams, cm
from matplotlib.pyplot import show, subplots, figure, subplot2grid
from matplotlib.ticker import ScalarFormatter
from matplotlib.gridspec import GridSpec
from numpy import arange, linspace, array, meshgrid, exp, cos, pi
from numpy.random import randn


def main():
    """
    main wrapper function
    """
    xnp = arange(0, 99)
    _, axes = subplots(1, 2, figsize=(10, 4))
    axes[0].plot(xnp, xnp**2, xnp, exp(xnp))
    axes[0].set_title("Normal scale")
    axes[1].plot(xnp, xnp**2, xnp, exp(xnp))
    axes[1].set_yscale("log")
    axes[1].set_title("Logarithmic scale (y)")

    _, axes = subplots(figsize=(10, 4))
    axes.plot(xnp, xnp**2, xnp, xnp**3, lw=2)
    axes.set_xticks([1, 2, 3, 4, 5])
    axes.set_xticklabels(
        [r"$\alpha$", r"$\beta$", r"$\gamma$", r"$\delta$", r"$\epsilon$"], fontsize=18
    )
    yticks = [0, 50, 100, 150]
    axes.set_yticks(yticks)
    axes.set_yticklabels([f"${y:.1f}$" for y in yticks], fontsize=18)

    _, axes = subplots(1, 1)
    axes.plot(xnp, xnp**2, xnp, exp(xnp))
    axes.set_title("scientific notation")
    axes.set_yticks([0, 50, 100, 150])
    formatter = ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((-1, 1))
    axes.yaxis.set_major_formatter(formatter)

    rcParams["xtick.major.pad"] = 5
    rcParams["ytick.major.pad"] = 5
    _, axes = subplots(1, 1)
    axes.plot(xnp, xnp**2, xnp, exp(xnp))
    axes.set_yticks([0, 50, 100, 150])
    axes.set_title("label and axis spacing")
    axes.xaxis.labelpad = 5
    axes.yaxis.labelpad = 5
    axes.set_xlabel("x")
    axes.set_ylabel("y")

    rcParams["xtick.major.pad"] = 3
    rcParams["ytick.major.pad"] = 3
    fig, axes = subplots(1, 1)
    axes.plot(xnp, xnp**2, xnp, exp(xnp))
    axes.set_yticks([0, 50, 100, 150])
    axes.set_title("title")
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    fig.subplots_adjust(left=0.15, right=0.9, bottom=0.1, top=0.9)

    _, axes = subplots(1, 2, figsize=(10, 3))
    axes[0].plot(xnp, xnp**2, xnp, xnp**3, lw=2)
    axes[0].grid(True)
    axes[1].plot(xnp, xnp**2, xnp, xnp**3, lw=2)
    axes[1].grid(color="b", alpha=0.5, linestyle="dashed", linewidth=0.5)


def main2():
    """
    main 2 wrapper function
    """
    xnp = arange(0, 99)
    _, axes = subplots(figsize=(6, 2))
    axes.spines["bottom"].set_color("blue")
    axes.spines["top"].set_color("blue")
    axes.spines["left"].set_color("red")
    axes.spines["left"].set_linewidth(2)
    axes.spines["right"].set_color("none")
    axes.yaxis.tick_left()

    _, ax1 = subplots()
    ax1.plot(xnp, xnp**2, lw=2, color="blue")
    ax1.set_ylabel(r"area $(m^2)$", fontsize=18, color="blue")
    for label in ax1.get_yticklabels():
        label.set_color("blue")
    ax2 = ax1.twinx()
    ax2.plot(xnp, xnp**3, lw=2, color="red")
    ax2.set_ylabel(r"volume $(m^3)$", fontsize=18, color="red")
    for label in ax2.get_yticklabels():
        label.set_color("red")

    _, axes = subplots()
    axes.spines["right"].set_color("none")
    axes.spines["top"].set_color("none")
    axes.xaxis.set_ticks_position("bottom")
    axes.spines["bottom"].set_position(("data", 0))
    axes.yaxis.set_ticks_position("left")
    axes.spines["left"].set_position(("data", 0))
    xxnp = linspace(-0.75, 1.0, 100)
    axes.plot(xxnp, xxnp**3)

    narr = array([0, 1, 2, 3, 4, 5])
    _, axes = subplots(1, 4, figsize=(12, 3))
    axes[0].scatter(xxnp, xxnp + 0.25 * randn(len(xxnp)))
    axes[0].set_title("scatter")
    axes[1].step(narr, narr**2, lw=2)
    axes[1].set_title("step")
    axes[2].bar(narr, narr**2, align="center", width=0.5, alpha=0.5)
    axes[2].set_title("bar")
    axes[3].fill_between(xnp, xnp**2, xnp**3, color="green", alpha=0.5)
    axes[3].set_title("fill_between")

    _, axes = subplots()
    axes.plot(xxnp, xxnp**2, xxnp, xxnp**3)
    axes.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
    axes.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green")

    fig, _ = subplots(2, 3)
    fig.tight_layout()

    fig = figure()
    subplot2grid((3, 3), (0, 0), colspan=3)
    subplot2grid((3, 3), (1, 0), colspan=2)
    subplot2grid((3, 3), (1, 2), rowspan=2)
    subplot2grid((3, 3), (2, 0))
    subplot2grid((3, 3), (2, 1))
    fig.tight_layout()


def main3():
    """
    main 3 wrapper function
    """
    xxnp = linspace(-0.75, 1.0, 100)
    fig = figure()
    for grs in GridSpec(2, 3, height_ratios=[2, 1], width_ratios=[1, 2, 1]):
        fig.add_subplot(grs)
    fig.tight_layout()

    fig, axes = subplots()
    axes.plot(xxnp, xxnp**2, xxnp, xxnp**3)
    fig.tight_layout()
    inset_ax = fig.add_axes([0.2, 0.55, 0.35, 0.35])
    inset_ax.plot(xxnp, xxnp**2, xxnp, xxnp**3)
    inset_ax.set_title("zoom near origin")
    inset_ax.set_xlim(-0.2, 0.2)
    inset_ax.set_ylim(-0.005, 0.01)
    inset_ax.set_yticks([0, 0.005, 0.01])
    inset_ax.set_xticks([-0.1, 0, 0.1])

    def flux_qubit_potential(phi_m, phi_p):
        alpha = 0.7
        phi_ext = 2 * pi * 0.5
        return (
            2 + alpha - 2 * cos(phi_p) * cos(phi_m) - alpha * cos(phi_ext - 2 * phi_p)
        )

    phi_m = linspace(0, 2 * pi, 100)
    phi_p = linspace(0, 2 * pi, 100)
    xmesh, ymesh = meshgrid(phi_p, phi_m)
    zmesh = flux_qubit_potential(xmesh, ymesh).T
    fig, axes = subplots()
    pic = axes.pcolor(
        xmesh / (2 * pi),
        ymesh / (2 * pi),
        zmesh,
        cmap=cm.RdBu,
        vmin=abs(zmesh).min(),
        vmax=abs(zmesh).max(),
    )
    fig.colorbar(pic, ax=axes)

    fig, axes = subplots()
    img = axes.imshow(
        zmesh,
        cmap=cm.RdBu,
        vmin=abs(zmesh).min(),
        vmax=abs(zmesh).max(),
        extent=[0, 1, 0, 1],
    )
    img.set_interpolation("bilinear")
    fig.colorbar(img, ax=axes)

    _, axes = subplots()
    axes.contour(
        zmesh,
        cmap=cm.RdBu,
        vmin=abs(zmesh).min(),
        vmax=abs(zmesh).max(),
        extent=[0, 1, 0, 1],
    )

    fig = figure(figsize=(14, 6))
    axes = fig.add_subplot(1, 2, 1, projection="3d")
    plo = axes.plot_surface(xmesh, ymesh, zmesh, rstride=4, cstride=4, linewidth=0)
    axes = fig.add_subplot(1, 2, 2, projection="3d")
    plo = axes.plot_surface(
        xmesh,
        ymesh,
        zmesh,
        rstride=1,
        cstride=1,
        cmap=cm.coolwarm,
        linewidth=0,
        antialiased=False,
    )
    fig.colorbar(plo, shrink=0.5)

    fig = figure(figsize=(8, 6))
    axes = fig.add_subplot(1, 1, 1, projection="3d")
    axes.plot_wireframe(xmesh, ymesh, zmesh, rstride=4, cstride=4)

    fig = figure(figsize=(8, 6))
    axes = fig.add_subplot(1, 1, 1, projection="3d")
    axes.plot_surface(xmesh, ymesh, zmesh, rstride=4, cstride=4, alpha=0.25)
    axes.contour(xmesh, ymesh, zmesh, zdir="z", offset=-pi, cmap=cm.coolwarm)
    axes.contour(xmesh, ymesh, zmesh, zdir="x", offset=-pi, cmap=cm.coolwarm)
    axes.contour(xmesh, ymesh, zmesh, zdir="y", offset=3 * pi, cmap=cm.coolwarm)
    axes.set_xlim3d(-pi, 2 * pi)
    axes.set_ylim3d(0, 3 * pi)
    axes.set_zlim3d(-pi, 2 * pi)


if __name__ == "__main__":
    main()
    main2()
    main3()
    show()
