import numpy as np
import pandas as pd


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


def mean_with_highest_removed(x):
    '''
    Drop the highest observation and take the mean

    >>> mean_with_highest_removed([0, 1, 2, 3])
    1

    '''
    x = np.array(x).copy()
    x.sort()
    return np.mean(x[:-1])


groups = pd.read_csv('data/groups.csv')
groups['moa'] = group_to_moa(groups['inches'])

# Throw out the worst group for each ammo type when taking the mean
groups['mean'] = groups['moa'].groupby(groups['ammo']).transform(mean_with_highest_removed)

groups.sort('mean', inplace=True)

if __name__ == '__main__':

    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.stripplot('ammo', 'moa', data=groups, jitter=True)
    plt.savefig('points.png')

    plt.clf()
    sns.boxplot('ammo', 'moa', data=groups)
    plt.savefig('boxplot.png')

    plt.clf()
    sns.barplot('ammo', 'mean', data=groups, ci=None)
    plt.title('mean moa for best 9 of 10 groups')
    plt.ylabel('moa')
    plt.savefig('avg_moa.png')
