# ------------------------------
# visualize_ambrose.py: Python file to visualize final Ambrose segmentation
#
# Run this file to visualize segmentation as produced by Concavity Measure 3D.ipynb
# Requires MayaVi to be downloaded, and the corresponding output folder in the cwd
# This zipfile folder is produced in the "MayaVi Output" section of Concavity Measure 3D.ipynb
#       Check that out for details on how to produce it and what information is inside
# ------------------------------


import numpy as np
import sys
import os
from mayavi import mlab

# to_color function assigns unique display color to each ID
# same as in Concavity Measure 3D.ipynb so as to match colors with 2D visualization
def to_color(n):
    return (((100.3729*n)%256) / 256, ((61.276*n)%256) / 256, ((113.7187*n)%256) / 256)


directory = './ambrose' # requires ambrose zipfile folder -- see above
for filename in os.listdir(directory):
    pts = np.load("./ambrose/" + filename)

    # produces separate lists for axes as MayaVi wants
    x = []; y = []; z = []
    for (i, j, k) in pts:
        x.append(i)
        y.append(j)
        z.append(k)

    key = int(filename[:-4]); print(key)
    # visualizes each cell as MayaVi point cloud, with same color as in 2D
    pts1 = mlab.points3d(x, y, z, scale_mode='none', scale_factor=8, color=to_color(key), opacity = 1)


# drawing the bounding box -- in practice, can use a point cloud
# and append points belonging to edges of rectangular prism
[xmax, ymax, zmax] = [770, 836, 149]
x = []; y = []; z = []

for i in [0, xmax]:
    for j in [0, ymax]:
        for k in range(zmax+1):
            x.append(i)
            y.append(j)
            z.append(k)
for j in [0, ymax]:
    for k in [0, zmax]:
        for i in range(xmax+1):
            x.append(i)
            y.append(j)
            z.append(k)
for k in [0, zmax]:
    for i in [0, xmax]:
        for j in range(ymax+1):
            x.append(i)
            y.append(j)
            z.append(k)

# draw bounding box as point cloud, as mentioned above
border = mlab.points3d(x, y, z, scale_mode='none', scale_factor=2, color=(0.1, 0.1, 0.1), opacity = 0.8)

# show the visualization -- will automatically pop up in a second window
mlab.show()
