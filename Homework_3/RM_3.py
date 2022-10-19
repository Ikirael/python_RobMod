import matplotlib.pyplot as plt
import numpy as np
import math

def derivative(f,x,eps = 0.01):
    return ((f(x+eps) - f(x))/eps)

t = np.arange(0,10,0.01)
y1 = np.sin(t)
y3 = derivative(np.sin, t[1])
y3 = [derivative(np.sin, i) for i in t]
plt.subplot(211)
plt.plot(t,y1,'b-.')
plt.subplot(212)
plt.plot(t,y3,'r--')
plt.show()