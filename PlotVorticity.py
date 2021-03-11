import h5py
import numpy as np 
from numpy import pi
import matplotlib.pyplot as plt
import cmocean 
import proplot 

plt.close('all')

# load simulation data
setup = h5py.File('output2/setup.h5','r')
snapshot = h5py.File('output2/snapshots/000000000000030.h5','r')

# plot vorticity 
kw = dict(cmap=cmocean.cm.balance,
          vmin=-20,vmax=20)
          
ticks = [0,pi/2,pi,3*pi/2,2*pi]
ticklabels = [r'0',r'$\pi/2$',r'$\pi$',
              r'$3\pi/2$',r'$2\pi$']

fig = plt.figure(figsize=(5,5))

ax = fig.add_subplot(111,aspect=1)

plt.pcolormesh(setup['grid/x'],
               setup['grid/z'],
               snapshot['q'],
               **kw
            )

plt.xticks(ticks,ticklabels)
plt.yticks(ticks,ticklabels)
plt.xlabel('x')
plt.ylabel('z')

plt.savefig('figure1a.png',bbox_inches='tight')
plt.savefig('figure1a.eps',bbox_inches='tight')
