import matplotlib.pyplot as plt
from math import sin, cos, pi
def plotfn(f, x):
    """
    :param f: function to plot
    :type f: callable
    :param x: values for x
    :type x: list or ndarray

    Plots the function f(x).
    """
    # yes, you can pass functions around as if
    # they were ordinary variables (they are)
    plt.plot(x, f(x))
    plt.xlabel("$x$-axis",fontsize=16)
    plt.ylabel("$f(x)$",fontsize=16)
    plt.title("Function $f(x)$")

def plotpolar(f,t, mint = -3*pi, maxt=6*pi)
    """
    :param f: function to plot
    :type f: callable
    :param t: values for t
    :type t: list or ndarray

    Plots the function r= f(t) on polar coordinates.
    """
    plt.plot(f(t)*cos(2*pi*t), f(t)*sin(2*pi*t))
    plt.xlabel("$x$-axis",fontsize=16)
    plt.ylabel("$y$-axis",fontsize=16)
    plt.title("Function $r= f(t)$")
