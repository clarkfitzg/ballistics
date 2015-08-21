import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def rads_to_moa(rads):
    '''
    Convert radians to minutes of angle
    '''
    degrees = rads * 180 / np.pi
    return 60 * degrees


def group_to_moa(groupsize, caliber=0.22, yardage=50):
    '''
    Convert group sizes in inches at a given yardage to MOA.

    Adjusts for caliber- so group should be measured from outside, not
    centers.
    '''
    groups = groupsize - caliber
    inches_to_target = yardage * 36
    theta = np.arctan(groups / inches_to_target)
    return rads_to_moa(theta)


groups = pd.read_csv('data/groups.csv')
groups['moa'] = group_to_moa(groups['inches'])

# Throw out the worst group for each ammo type
# Would do that if calculating confidence intervals

ax0 = plt.subplot(121)
sns.stripplot('ammo', 'moa', data=groups, jitter=True)
ax0.set_ylim(0, 5)

ax1 = plt.subplot(122)
sns.boxplot('ammo', 'moa', data=groups)
ax1.set_ylim(0, 5)

plt.savefig('groups.png')
