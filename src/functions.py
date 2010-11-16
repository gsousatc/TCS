#!/usr/bin/ python
# -*- coding:ISO-8859-1 -*-

# Copyright (c) 2010 GC, RL. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

__author__="Gon�alo Carvalhal <gsousatc@itn.pt>"
__author__="                  <        @itn.pt>"
__version__="0.1"
__date__="Nov 10 2010"


from mpl_toolkits.mplot3d import axes3d, Axes3D
import math
import matplotlib.pyplot as plt
import numpy as np
import random

# system definition
# system definition (origin)
x0=0
y0=0
z0=0
origin=(x0, y0, z0)

# system definition (source)
xs=0
ys=0
zs=0
source=(xs, ys, zs)

nps=2
e_cutoff=10



# TODO: read mu from file
mu=random.random()


def distance(x1, y1, z1, x2, y2, z2):
    """Calculates distance between 2 points
    
    """
    return math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

def path(T = 100, period = 1):
    """Makes path and calculates its length

    """
    #source
    x, y, z=source 

    answer=[[0, 0, 0]]
    X=[x]
    Y=[y]
    Z=[z]
    
    # plotting
    fig=plt.figure()
    ax=Axes3D(fig)
    
    # plotting (axes)
    ax.set_xlabel('XX')
    ax.set_ylabel('YY')
    ax.set_zlabel('ZZ')
    
    
    d=0
    x1, y1, z1=x0, y0, z0
    
    #TODO: do while runs < nps
    #TODO: do while E > e_cutoff
    for t in xrange(T):
        
        # direction cossines
        costheta_x=random.uniform(-1, 1)
        costheta_y=random.uniform(-1, 1)
        costheta_z=random.uniform(-1, 1)       
        
        dx=(1/mu)*costheta_x
        dy=(1/mu)*costheta_y
        dz=(1/mu)*costheta_z
#        print dx, mu
#        print dy, mu
#        print dz, mu    
        
        
        x+=dx
        y+=dy
        z+=dz
        
        d+=distance(x1, y1, z1, x, y, z)
        
        x1, y1, z1=x, y, z
                
        answer.append([t+1, x, y, z])
        X.append(x)
        Y.append(y)
        Z.append(z)   

            
    ax.scatter3D(X[1:2], Y[1:2], Z[1:2], c = 'r', marker = 's', linewidths = 1)
    ax.scatter3D(X, Y, Z, c = 'b', marker = 'o', linewidths = 1)
    
    d=distance(x, y, z, x0, y0, z0)  
    
    print "Initial position: ", "(%.2f,%.2f,%.2f)"%(X[0], Y[0], Z[0])
    print "Final position: ", "(%.2f,%.2f,%.2f)"%(X[-1], Y[-1], Z[-1])
    print "N� steps: ", t+1
    print "Total path length: ", d
    
    
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(X[0], Y[0], 's', color = 'g', ms = 9)
    ax.plot(X, Y, '-o', color = 'b', ms = 4)
    ax.plot(X[-1], Y[-1], 's', color = 'r', ms = 9)
    plt.show()
   
    #summary()    
    
    
    return answer


#TODO: plot step number t

for n in range(1, nps+1):
    print n, nps
    path()
