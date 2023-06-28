import control as con
import matplotlib.pyplot as plt
import numpy as np

A = -40
B = 2.8
C = 90

num = np.array([1])
# den = np.array([ 1, (B-A), (A*B*C), -A*C])
den = np.array([ 1, 2])

sys = con.TransferFunction(num,den)
time_simulation = np.arange( 0, 15, 0.5, dtype = float)

[xout, yout] = con.step_response(sys,time_simulation)

plt.figure()
plt.plot(xout, yout)
plt.show()
