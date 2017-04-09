import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

print "begin"

# put data in numpy array
with open('signal.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
y = np.asarray(lines)

#do fft
yf = fft(y)

#stuff for x axes
N = len(lines) #number of samples
T = 1.0/3000.0 #sample spacing
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

# raw data plot
#x = np.linspace(0, N*T, N)
#plt.plot(x,y)
#plt.grid()
#plt.show()

#fft plot
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()
plt.show()
