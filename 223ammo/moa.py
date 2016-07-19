import numpy as np
import pandas as pd


def rads_to_moa(rads):
    '''
    Convert radians to minutes of angle
    '''
    degrees = rads * 180 / np.pi
    return 60 * degrees


def group_to_moa(groupsize, caliber=0.22, distance=100, units="meters"):
    '''
    Convert group sizes in inches at a given yardage to MOA.

    Adjusts for caliber- so group should be measured from outside, not
    centers.
    '''
    groups = groupsize - caliber
    if units == "meters":
        yardage = distance * 1.09361
    inches_to_target = yardage * 36
    theta = np.arctan(groups / inches_to_target)
    return rads_to_moa(theta)


def main():
    df = pd.read_csv("groups.csv")
    df["moa"] = group_to_moa(df.loc[:, ["inches"]])
    return df


if __name__ == "main":

    main()
