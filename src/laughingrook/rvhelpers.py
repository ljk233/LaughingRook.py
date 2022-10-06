
import numpy as np
import pandas as pd
from scipy.stats import rv_continuous, rv_discrete
from numpy.typing import NDArray


# ======================================================================
# PUBLIC
# ======================================================================


def minmax(rv: rv_continuous | rv_discrete) -> tuple:
    """Return the min, max values of rv.

    If a min, max value is undefined, then its value is approximated to
    min=0.001-quantile, max=0.999-quantile.
    """
    a, b = rv.a, rv.b
    if a == -np.inf:
        a = rv.ppf(0.001)
    if b == np.inf:
        b = rv.ppf(0.999)
    return a, b


def continuous_xs(rv: rv_continuous) -> NDArray:
    """Return the event space of the given continuous rv.

    If a min, max (a, b) value is undefined, then its value is
    approximated to min=0.001-quantile, max=0.999-quantile.

    If rv is a discrete random variable, then an argument for step
    should be passed.
    """
    a, b = minmax(rv)
    return np.linspace(a, b, 1000)


def discrete_xs(rv: rv_discrete, step: int = 1) -> NDArray:
    """Return the event space of the given discrete rv.

    If a step is pass, then ....

    If a min, max (a, b) value is undefined, then its value is
    approximated to min=0.001-quantile, max=0.999-quantile.
    """
    a, b = minmax(rv)
    return np.arange(a, b+1, step=step, dtype=int)


def probability_table(rv: rv_discrete) -> pd.DataFrame:
    """Return a probability table for the given rv.
    If rv is a discrete random variable, then an argument for step
    should be passed.
    """
    xs = discrete_xs(rv)
    data = [rv.pmf(xs), rv.cdf(xs)]
    columns = pd.Index(xs, name=rv.name)
    index = ['pmf', 'cdf']
    return pd.DataFrame(
            data,
            columns=columns,
            index=index
    )


def describe(rv: rv_continuous | rv_discrete, ret_dtype=object) -> pd.Series:
    """Return a descriptive table for the given rv.

    Te return series has dtype=object by default.
    This is done to promote the trimming of trailing zeros.
    The given ret_dtype will be passd to the Series constructor, so it
    should be a valid pandas dtype.
    """
    stats = {'mean': rv.mean(),
             'var': rv.var(),
             'min': rv.a,
             'lq': rv.ppf(0.25),
             'med': rv.median(),
             'uq': rv.ppf(0.75),
             'max': rv.b}
    return pd.Series(stats, name=rv.name, dtype=ret_dtype)


def iqr(rv: rv_continuous | rv_discrete, ret_dtype=object) -> pd.Series:
    """Return the interquartle range, upper - lower quartiles.
    """
    return rv.ppf(0.75) - rv.ppf(0.25)
