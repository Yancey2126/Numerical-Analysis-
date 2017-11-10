import numpy as np
from matplotlib import pyplot as plt

# Define the example function
def f(x):
    return np.sin(np.exp(x))
    #return np.sin(x)
    
#print f(0.)

x = np.linspace(0,2,400)
plt.plot(x, f(x))
plt.plot(x, np.zeros_like(x), "k--")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title('Function f(x) = sin(e^x)')
plt.show()

# Define the Trapezoidal rule
def Trapezoidal(f, a, b):
    I = ((b-a)/2)*(f(a) + f(b))
    return I

print 'Trapezoidal gives ' + str(Trapezoidal(f, 0., 2.))

# The Composite Trapezoidal Rule with N subintervals on [0,2]
def Com_Trap(N):
    I = 0
    for i in range(0, N):        
        h = 2./N
        xi = i*h
        xiplus = (i + 1)*h
        #print str(xi), str(xiplus)
        Ii = Trapezoidal(f, xi, xiplus)
        #print 'On interval ' + str(i) +', Trapezoidal gives ' + str(Ii)
        I = I + Ii
    return I

# Calculate with h = 1/10, 1/20, 1/40
for N in [20, 40, 80]:
    IN = Com_Trap(N)
    print 'with h = ' + str(2./N) +':'
    print 'Composite Trapezoidal Rule approximation is : ' + str(IN)
    I2N = Com_Trap(2*N)
    I4N = Com_Trap(4*N)
    R = (IN - I2N) / (I2N - I4N)
    print 'R ratio is: ' + str(R)


# Code up Simpson's Rule
def Simpson(f, a, b):
    m = (a + b) / 2
    I = (b-a)/6*(f(a) + 4*f(m) + f(b))
    return I
    
#print 'Simpson gives ' + str(Simpson(f, 0., 2.))

# Call Simpson's in composite rules
def Com_Simp(N):
    I = 0
    for i in range(0, N):        
        h = 2./N
        xi = i*h
        xiplus = (i + 1)*h
        #print str(xi), str(xiplus)
        Ii = Simpson(f, xi, xiplus)
        #print 'On interval ' + str(i) +', Trapezoidal gives ' + str(Ii)
        I = I + Ii
    return I

# Test out
for N in [20, 40, 80]:
    IN = Com_Simp(N)
    print 'with h = ' + str(2./N) +':'
    print 'Composite Simpson Rule approximation is : ' + str(IN)
    I2N = Com_Simp(2*N)
    I4N = Com_Simp(4*N)
    R = (IN - I2N) / (I2N - I4N)
    print 'R ratio is: ' + str(R)