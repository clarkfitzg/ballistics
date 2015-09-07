import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


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


def postprocess(rotation=30):
    '''
    Rotate labels on the current x axis
    '''
    ax = plt.gca()
    for label in ax.get_xticklabels():
        label.set_rotation(rotation)
    plt.tight_layout()


def read_groups(datafile='data/groups.csv'):
    '''
    Read and perform calculations on the groups
    '''

    groups = pd.read_csv(datafile)
    groups['moa'] = group_to_moa(groups['inches'])

    # Flag the largest group for each type of ammo
    groups['largest'] = (groups['moa']
                         .groupby(groups['ammo'])
                         .transform(lambda x: x == max(x))
                         .astype(bool)
                         )

    # Throw out the worst group for each ammo type when taking the mean
    groups['mean'] = (groups['moa']
                      .groupby(groups['ammo'])
                      .transform(mean_with_highest_removed)
                      )

    # Standardize each to see if normal approximation holds
    groups['standard'] = (groups['moa']
                          [~groups['largest']]
                          .groupby(groups['ammo'])
                          .transform(stats.zscore, ddof=1)
                          )

    groups.sort('mean', inplace=True)

    return groups


def make_plots(groups):

    sns.stripplot('ammo', 'moa', data=groups, jitter=True)
    postprocess()
    plt.savefig('points.png')

    plt.clf()
    sns.boxplot('ammo', 'moa', data=groups)
    postprocess()
    plt.savefig('boxplot.png')

    plt.clf()
    sns.barplot('ammo', 'mean', data=groups, ci=None)
    plt.title('mean moa for best 9 of 10 five shot groups')
    plt.ylabel('moa')
    postprocess()
    plt.savefig('avg_moa.png')

    plt.clf()
    std = groups['standard']
    std = std[std.notnull()]

    fig, axes = plt.subplots(ncols=2)
    sns.distplot(std, ax=axes[0])
    stats.probplot(std, plot=axes[1])
    fig.set_size_inches(6, 4)
    fig.tight_layout()
    plt.savefig('qqplot.png')


def print_stats(groups):
    '''
    Print fitted model comparing sk rifle match as intercept and 
    eley edge as treatment
    '''

    ammo = groups['ammo']
    twobest = (groups[(ammo == 'sk rifle match')
                      | (ammo == 'eley edge black')]).copy()

    # Can't figure out how to set reference level for anova model
    # so do it manually
    twobest['eley'] = (twobest['ammo'] == 'eley edge black')

    model = smf.ols('moa ~ eley', data=twobest,
            subset=np.logical_not(twobest['largest']))

    print(model.fit().summary())


def main():

    groups = read_groups()
    make_plots(groups)
    print_stats(groups)


if __name__ == '__main__':

    main()
