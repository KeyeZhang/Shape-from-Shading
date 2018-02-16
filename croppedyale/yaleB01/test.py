import os
import sys
import glob
import re
import numpy as np
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

x = np.asarray(Image.open("yaleB01_P00_Ambient.pgm"))
y = np.asarray(Image.open("yaleB01_P00A-005E-10.pgm"))
print(mat(x))
print((mat(y)))
print(mat(x) - mat(y))
