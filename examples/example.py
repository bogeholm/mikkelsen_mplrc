""" mikkelsen_mplrc example
"""

import mikkelsen_mplrc as mkl
import numpy as np
import matplotlib.pyplot as plt

__author__ = "Troels Bogeholm Mikkelsen"
__copyright__ = "Troels Bogeholm Mikkelsen 2016"
__credits__ = "matplotlib.org"
__license__ = "MIT"
__version__ = "0.1"
__email__ = "bogeholm@nbi.ku.dk"
__status__ = "Development"

# Saving three different figures
plt.ion()
plt.close('all')

# Generate data - random walk
np.random.seed(42*42)
noise = np.random.randn(1000)
x = np.cumsum(noise)
bluish = '#2976bb' # https://xkcd.com/color/rgb/

# paper mode
mkl.paper()

fig1, ax1 = plt.subplots(1, 1)
ax1.plot(x, label='Drunken Walk', c=bluish)
ax1.set_xlabel(r'$t$')
ax1.set_ylabel(r'$x(t)$')
ax1.set_title(r'paper()')
ax1.legend()
plt.draw()

# presentation mode
mkl.presentation()

fig2, ax2 = plt.subplots(1, 1)
ax2.plot(x, label='Drunken Walk', c=bluish)
ax2.set_xlabel(r'$t$')
ax2.set_ylabel(r'$x(t)$')
ax2.set_title(r'presentation()')
ax2.legend()
plt.draw()


# Save?
fig1.savefig('paper.png', transparent=True, bbox_inches='tight', dpi=600)
fig2.savefig('presentation.png', transparent=True, bbox_inches='tight', dpi=600)

# default
mkl.mpldefaults()
plt.ion()

fig3, ax3 = plt.subplots(1, 1)
ax3.plot(x, label='Drunken Walk', c=bluish)
ax3.set_xlabel(r'$t$')
ax3.set_ylabel(r'$x(t)$')
ax3.set_title('mpldefaults()')
ax3.legend()
plt.draw()

# Save?
fig3.savefig('mpldefaults.png', transparent=True, bbox_inches='tight', dpi=600)
