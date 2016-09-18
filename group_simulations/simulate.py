import numpy as np

import matplotlib.pyplot as plt

# In this simulation we model the variance of bullet impact position (call
# it P) from a rifle relative to the point of aim using 2 Gaussian random
# variables, one for each of the horizontal (x) and vertical (y)
# components.
# 
# To determine experimentally whether this model is reasonable one should
# go to the range under ideal conditions (ie. experienced shooter with
# accurate gun / ammunition and very little wind), fire 100 or so rounds
# and measure the x and y positions of each shot. Then QQ plots can be used
# to check normality. Long distance benchrest or F class matches might be
# an ideal place to gather this data.

# Goal 1
# Establish relationships between the following components:
# - Standard deviation of P
# - 5 shot group size
# - k shot group size

# Goal 2
# Use the model for P to numerically calculate the probability of hits on
# various targets.

# Goal 3
# How common are groups with fliers? This means that four shots are close,
# while 1 is far from the others.

# Sources of variance under consideration. Values correspond to standard
# deviation in each component (x, y)

sd = {"rifle": (1, 1),
      "wind": (0.5, 0),
      "elev": (0, 0.1),
      "hold": (0.1, 0.1),
      }

vx = sum(v[0] ** 2 for v in sd.values())
vy = sum(v[1] ** 2 for v in sd.values())


def simulate(vx=1, vy=1, cov_xy=0, n=5):
    """
    Simulate the position of n shots. Returns an n x 2 matrix where the
    rows correspond to (x, y) position
    """
    cov = np.array(((vx, cov_xy), (cov_xy, vy)))
    xy = np.random.multivariate_normal((0, 0), cov, n)
    return xy


plt.plo
