"""
This modules contains the exercises of the testing notebook.
In order to execute the tests, open the Jupyter filebrowser to the left, click on the big plus icon at the top and select 'Terminal'. In the terminal, navigate to the folder that contains this file. Then, use

    pytest
    
to run all tests.
You can select a test to run via

    pytest -k test_name
    
Pytest will locate tests in all Python files whose name begins with 'test_'.
We create a test case by defining a function with a name that also starts with 'test_'.

Note that in this case, the functions which we want to test are defined in the test module. This is only so in order to simplify the exercises. Normally, we would use separate modules to define functions with our business logic and the tests.
"""


import numpy as np
import pytest
from scipy.constants import golden, neutron_mass


############################################################
#                      FIBONACCI

def fibonacci(n):
    """
    Return the nth Fibonacci number.
    """
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def test_fibonacci():
    # -- YOUR CODE HERE --    
    pytest.skip()


############################################################
#                      LEAP YEARS

def is_leapyear(year):
    """
    Return True if year is a leap year, False otherwise.
    """
    return year % 400 == year % 100 + year % 4 != 0


def test_is_leapyer():
    # -- YOUR CODE HERE --    
    pytest.skip()


############################################################
#                   HISTOGRAMMING

def histogram(data, bin_edges):
    """
    Construct a histogram of one dimensional data.
    
    Arguments:
      data: 1D array.
      bin_edges: (len=nbins+1) 1D array of bin edges.
                  Bin i is in range [bin_edges[i], bin_edges[i+1]].
    """
    hist = np.zeros(shape=[len(bin_edges)-1], dtype=int)
    for value in data:
        for i in range(1, len(bin_edges)):
            if value < bin_edges[i]:
                hist[i-1] += 1
                break
    return hist


def test_histogram():
    # -- YOUR CODE HERE --    
    pytest.skip()


############################################################
#                   CHI SQUARED

def chi_squared(model, meas, errors):
    return np.sum(((model - meas)/errors)**2)


def test_chi_squared():
    # -- YOUR CODE HERE --    
    pytest.skip()


############################################################
#                 LEAST SQUARES FIT*

def fit_parabola(x, y_meas, errors, start_params):
    """
    Perform a least squares fit of a parabola.
    
    Arguments:
      x: Independent variable.
      y_meas: measured values of the dependent variable.
      errors: Uncertainties of the measured values.
      start_params: (len=3) Iniitla values for the parameters of the parabola.
      
    Returns:
      Best fit results for the parameters of the parabola.
    """
    X = np.array([np.ones_like(x), x, x**2]).T
    V = np.diag(1/errors**2)
    return np.linalg.inv(X.T @ V @ X) @ X.T @ V @ y_meas


def test_fit_parabola():
    # -- YOUR CODE HERE --    
    pytest.skip()


############################################################
#                   ENERGY TRANSFER

def energy_transfer(ei_or_ef, tof, L1, L2, mode):
    """
    Compute the energy transfer for inelastic neutron scattering.
    
    All units are SI.
    
    Arguments:
      ei_or_ef: In direct scattering: the initial energy.
                In indirect scattering: the final energy.
      tof: Time-of-flight.
      L1: Primary flight path.
      L2: Secondary flight path.
      mode: Either 'direct' or 'indirect'.
    """
    t0 = np.sqrt(L1**2 * neutron_mass / ei_or_ef)
    delta_t = tof - t0
    if mode == 'direct':
        return ei_or_ef - neutron_mass * L2**2 / 2 / delta_t**2
    elif mode == 'indirect':
        return ei_or_ef - neutron_mass * L1**2 / 2 / delta_t**2


def test_energy_transfer():
    # -- YOUR CODE HERE --    
    pytest.skip()
