import numpy as np
from scipy import signal
import pylab as pl

t = np.linspace(0,10,1000)
x = signal.chirp(t,5,10,30)
pl.plot(t,x)
pl.show()
