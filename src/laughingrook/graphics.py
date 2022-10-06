
import numpy as np
from matplotlib import pyplot as plt
from numpy.typing import ArrayLike


# ======================================================================
# PRIVATE
# ======================================================================


def _plot_single_axis(title: str, xlab: str, ylab: str):
    """Shared functions for completing the plot where there is a single
    axis.
    """
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.tight_layout()
    plt.show()


# ======================================================================
# PUBLIC
# ======================================================================


def std_lineplot(x: ArrayLike, y: ArrayLike, title: str, xlab: str, ylab: str):
    """Plot a line plot of the given rv.

    This is an opinionated convenience function.
    """
    plt.plot(x, y)
    _plot_single_axis(title, xlab, ylab)



def std_stemplot(x: ArrayLike, y: ArrayLike, title: str, xlab: str, ylab: str):
    """Plot a stemplot for the given x, y.

    This is an opinionated convenience function.
    It is assumed that x = [a, a+1, a+2, ..., a+n].
    """
    plt.stem(y, basefmt=" ")
    plt.xticks(np.arange(0, len(x)), x)
    _plot_single_axis(title, xlab, ylab)
