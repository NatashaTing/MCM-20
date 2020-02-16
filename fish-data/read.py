
import datetime as dt  # Python standard library datetime  module
import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, addcyclic, shiftgrid

import pandas as pd

def main():
    path = 'OfficialNominalCatches_16Sep2019/ICESCatchDataset2006-2017.csv'
    # f = open('OfficialNominalCatches_16Sep2019/ICESCatchDataset2006-2017.csv', 'r')
    dat = pd.read_csv(path)
    print(type(dat))


if __name__== "__main__":
    main()

