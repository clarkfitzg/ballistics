"""
What's the difference in weight between different barrel contours?
"""

import numpy as np

# density of steel converted to lbs / in^3
STEEL_DENSITY = 4.5 / 16


def barrelwt(length=26, caliber=0.22, muzzle_diam=0.8, shank_diam=1.055):
    """
    Approximate weight in lbs for straight tapered barrel
    """
    r1, r2 = shank_diam / 2, muzzle_diam / 2
    shank_area = np.pi * r1 ** 2 - np.pi * caliber ** 2
    cylinderwt = shank_area * length
    contourwt = np.pi * (r1 ** 2 - r2 ** 2) * length / 3
    return (cylinderwt - contourwt) * STEEL_DENSITY


if __name__ == '__main__':

    barrelwt(muzzle_diam=1)

    barrelwt(length=24, muzzle_diam=0.75)

    barrelwt(length=24, muzzle_diam=0.8)

    weights = {'savage target action': 2.375,
               'hs precision stock PSV106': 3.06,
               'sightron siii 6-24 x 50': 24.3 / 16,
               }

    prices = {'savage target action': 550,
               'hs precision stock PSV106': 330,
               'mcgowen barrel': 325,
               'sightron siii 6-24 x 50': 800,
               'seekins base and rings': 200,
               }

    sum(x for x in weights.values())

    sum(x for x in prices.values())
