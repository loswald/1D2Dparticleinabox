import numpy as np
import matplotlib.pyplot as plt

print ("Enter Length of 1D Potential Well in Nanomet")

lengthxstring = input()
lengthx = float(lengthxstring)

print ("Enter Energy Level")
nstring = input()
n = float(nstring)

x = np.arange(0., lengthx, (lengthx-0)/1000)
psi = np.sqrt(2/lengthx)*np.sin((x)*(n*3.14/lengthx))
plt.plot(x, psi)
plt.ylabel('WAVE FUNCTION')
plt.xlabel('LOCATION')
plt.show()
