# ------------------------------
# visualize_3d.py: Python file to visualize concavity algorithm behavior
#
# Upon running, will ask for a key -- format "i j" where i < j
#       to visualize the border between cell segment ID i and cell segment ID j
# Requires MayaVi to be downloaded, and the corresponding zipfile folder in the cwd
# This zipfile folder is produced in the "MayaVi Output" section of Concavity Measure 3D.ipynb
#       Check that out for details on how to produce it and what information is inside
# ------------------------------


# Create the data.
import numpy as np
import sys

keyname = input("Key (\"i j\" where i < j): ")
try:
    arrshape = np.load("./" + keyname + "/arrshape.npy")
except:
    print("Key not found. Have you exported this test case in Concavity Measure 3D yet? Exiting..."); sys.exit()

show_bounding_box = True # show bounding box representing borders of the current dataset slice
show_edge_checks = False # show edge check points before step -- see Concavity Measure 3D.ipynb for more details

c1 = np.load("./" + keyname + "/cell_1.npy")
c2 = np.load("./" + keyname + "/cell_2.npy")
border_list = np.load("./" + keyname + "/borderlist.npy") 
scan_list = np.load("./" + keyname + "/scanlist.npy")
scan_list_f = np.load("./" + keyname + "/scanlist_f.npy")
edgelist = np.load("./" + keyname + "/edgelist.npy")
[a,b,c,d] = np.load("./" + keyname + "/plane.npy")

# changing plane notation to ax + by + c = z, easier to display
[a,b,c] = [-1*a/c, -1*b/c, d/c]
[xmax, ymax, zmax] = arrshape

xp = np.zeros((xmax, ymax))
yp = np.zeros((xmax, ymax))
zp = np.zeros((xmax, ymax))
mask = np.full((xmax, ymax), True)

x = [[],[],[], [],[],[],[]]
y = [[],[],[], [],[],[],[]]
z = [[],[],[], [],[],[],[]]

# list designed to readin information into MayaVi objects
# appends pixel dimensions into separate lists as MayaVi wants
stuff_list = [c1, c2, border_list, scan_list, scan_list_f, edgelist]
for t in range(6):
    for (i, j, k) in stuff_list[t]:
        x[t].append(i)
        y[t].append(j)
        z[t].append(k)

# constructs the pixel map for the plane -- recall it's in ax + by + c = z format
# the mask restricts the plane visualization to the bounding box -- makes visualization easier
for i in range(xmax):
    for j in range(ymax):
        xp[i, j] = i
        yp[i, j] = j
        zp[i, j] = c + a*i + b*j

        # plane is implicitly restricted within the box on x-axis/y-axis
        # mask is required to restrict within the box on z-axis
        if 0 <= zp[i, j] < zmax:
            mask[i, j] = False


# bounding box construction
# simply adds points belonging to the rectangular prism making up the bounding box
border = []
for i in [0, xmax]:
    for j in [0, ymax]:
        for k in range(zmax+1):
            x[6].append(i)
            y[6].append(j)
            z[6].append(k)
for j in [0, ymax]:
    for k in [0, zmax]:
        for i in range(xmax+1):
            x[6].append(i)
            y[6].append(j)
            z[6].append(k)
for k in [0, zmax]:
    for i in [0, xmax]:
        for j in range(ymax+1):
            x[6].append(i)
            y[6].append(j)
            z[6].append(k)


# takes all the information above, and builds MayaVi objects out of them
# most of them are point clouds (hence the efficiency requirement on the cells); the plane can be a mesh
from mayavi import mlab
pts1 = mlab.points3d(x[0], y[0], z[0], scale_mode='none', scale_factor=2, color=(0, 0, 0.7), opacity = 0.2)

pts2 = mlab.points3d(x[1], y[1], z[1], scale_mode='none', scale_factor=2, color=(0, 0.7, 0), opacity = 0.2)

pts3 = mlab.points3d(x[2], y[2], z[2], scale_mode='none', scale_factor=2, color=(1, 1, 1), opacity = 1)
mesh3 = mlab.pipeline.delaunay2d(pts3)
surf3 = mlab.pipeline.surface(mesh3, color = (1, 1, 1), opacity = 0)

mesh4 = mlab.mesh(xp, yp, zp, color = (0.3, 0.3, 0.3), opacity = 0.6, mask = mask)

pts5 = mlab.points3d(x[3], y[3], z[3], scale_mode='none', scale_factor=2, color=(1, 0, 0), opacity = 1)
pts6 = mlab.points3d(x[4], y[4], z[4], scale_mode='none', scale_factor=2, color=(1, 0.8, 0.8), opacity = 1)
if show_edge_checks:
    pts7 = mlab.points3d(x[5], y[5], z[5], scale_mode='none', scale_factor=3, color=(1, 1, 0), opacity = 1)

if show_bounding_box:
    border = mlab.points3d(x[6], y[6], z[6], scale_mode='none', scale_factor=2, color=(0.1, 0.1, 0.1), opacity = 0.8)


mlab.show()