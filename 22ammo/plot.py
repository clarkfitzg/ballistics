import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

groups = pd.read_csv('data/groups.csv')

sns.factorplot('ammo', 'inches', data=groups)


def group_yards_to_moa(groupsize, caliber=0.22, yardage=50):
    '''
    Convert a vector of group sizes in inches at a given yardage to MOA.

    Adjusts for caliber- so group should be measured from outside, not
    centers.
    '''
    groups = groupsize - caliber
