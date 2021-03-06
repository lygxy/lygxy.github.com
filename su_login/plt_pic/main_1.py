#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from config_1 import *

def num_to_pic(csv_name):
    data = pd.read_csv(csv_name)

    plt.scatter(data.Sn, data.Num)
    plt.plot(data.Sn, data.Num)
    plt.show()

    exit()

def main():
    f_name = FILE_NAME
    num_to_pic(f_name)

if __name__ == '__main__':
    main()
