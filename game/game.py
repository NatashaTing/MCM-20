import nashpy as nash
import numpy as np


A = 1
B = 2
p = 0.25
C = 3

a11 = A/2 + p*B
a12 = A + p*B
a21 = p*B
a22 = p*C

b11 = A/2 + p*B
b12 = p*B
b21 = A + p*B
b22 = p*C

A = np.array([[a11, a12], [a21, a22]])
B = np.array([[b11, b12], [b21, b22]])
rps = nash.Game(A, B)

sigma_r = [1, 0]  # play scissors
sigma_c = [0, 1]  # play paper
print('payoffs are' ,rps[sigma_r, sigma_c])

eqs = rps.support_enumeration()
print('equilibrium is', list(eqs))


