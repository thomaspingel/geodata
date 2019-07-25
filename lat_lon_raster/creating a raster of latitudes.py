# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:56:03 2018

@author: Thomas Pingel
"""

#%%
import rasterio
import numpy as np

cellsize = .1
xedges = np.arange(-180,180,cellsize)
yedges = np.arange(90,-90,-cellsize)
XI, YI = np.meshgrid(xi,yi)

t = rasterio.transform.from_origin(xedges[0], yedges[0], cellsize, cellsize)

with rasterio.open('latitude.tif', 'w', driver='GTiff', 
                             height=YI.shape[0], width=YI.shape[1],
                             count=1, dtype=np.float32, transform=t) as src:
    src.write(YI.astype(np.float32), 1)
    
with rasterio.open('latitude_abs.tif', 'w', driver='GTiff', 
                             height=YI.shape[0], width=YI.shape[1],
                             count=1, dtype=np.float32, transform=t) as src:
    src.write(np.abs(YI).astype(np.float32), 1)
    
    