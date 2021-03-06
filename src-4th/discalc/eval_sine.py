from numpy import *
import sys

xp = eval(sys.argv[1])
n = int(sys.argv[2])

def S_k(k):
    return s[k] + \
           ((s[k+1] - s[k])/(x[k+1] - x[k]))*(xp - x[k])
h = pi/n
x = linspace(0, pi, n+1)
s = sin(x)
k = int(xp/h)

print 'Approximation of sin(%s):  ' % xp, S_k(k)
print 'Exact value of sin(%s):    ' % xp, sin(xp)
print 'Eror in approximation:     ', sin(xp) - S_k(k)
