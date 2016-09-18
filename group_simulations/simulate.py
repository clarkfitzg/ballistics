import numpy as np

# In this simulation we model bullet impact position (call it P) from a
# rifle relative to the point of aim using 2 Gaussian random variables, one
# for each of the horizontal (x) and vertical (y) components.

# Goal 1
# Establish relationships between the following components:
# - Standard deviation of P
# - 5 shot group size
# - k shot group size

# Goal 2
# Use the model for P to numerically calculate the probability of hits on
# various targets.

# The primary sources of variance. Values correspond to variance in each
# component (x, y)
variance = {"rifle": (1, 1),
            "wind": (0.5, 0),
            "elev": (0, 0.1),
            "hold": (0.1, 0.1),
            }

vx = sum(v[0] for v in variance.values())
vy = sum(v[1] for v in variance.values())

