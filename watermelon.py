# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:32:12 2022

@author: hp
"""

import matplotlib.pyplot as plt
data=[[10,10,10,10,10,10,10,10,10,10,10]],
[10,10,10,10,10,10,10,5,10,10,10],
[10,10,10,10,10,10,9,6,5,10,10,10],
[10,10,10,10,10,9,10,10,6,5,10,10],
[10,10,10,10,9,10,10,10,6,5],
[10,10,10,9,10,10,10,10,6,5],
[10,10,9,10,10,10,10,10,6,5],
[10,9,10,10,10,10,10,10,6,5,5],
[9,1,10,10,10,10,10,10,10,5,5],
[6,10,10,10,10,10,10,10,10,5],
[10,5,6,6,6,6,6,6,6,5,10,10,10,10],
[10,10,10,5,5,5,5,5,5,5,10,10,10,10]

      
plt.imshow(data, cmap="nipy_spectral")