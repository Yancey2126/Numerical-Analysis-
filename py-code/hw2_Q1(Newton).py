# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

tol = 1e-12  # If the "residual" |f(x_k)| < tol, stop iteration

def f(x):
# Basic idea, superlinear convergence, comparing Newton, Secant, and Newton2:
    #return np.exp(x) - x - 2
    #return x**2 - 2
    return np.sin(x**2) + 1.02 - np.exp(-x)
       
def f_prime(x):
    #return np.exp(x) - 1
    #return 2*x
    return 2*x*np.cos(x**2) + np.exp(-x)

x = np.linspace(-1., 5., 400)
plt.plot(x,f(x))
plt.plot(x,np.zeros_like(x),'k-')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Image of f(x)')
plt.show()
            
    

def Newton(x0):

    # Take an initial guess:    
    xk = x0
    
    xk_list=[xk]
    residual_list=[abs(f(xk))]    
    residual = abs(f(xk))
    
    
    while residual>tol:
        
        xk = xk - f(xk)/f_prime(xk)
        residual = abs(f(xk))
        
        xk_list.append(xk)
        residual_list.append(residual)
        
        print xk, residual
        
    return xk_list, residual_list
    
    
xk_list, residual_list = Newton(x0=-1.)

print 'Number of iterations = ', len(xk_list)


Plotting = True

if Plotting:
               
    fig = plt.figure(2)
    plt.plot(xk_list,'o')
    plt.xlabel('k')
    plt.ylabel('$x_k$')
    plt.title('Newton\'s Method Iteration --- x_k ')
    plt.legend(loc='upper right')
    plt.show()
    

    fig = plt.figure(3)
    plt.plot(np.log10(np.array(residual_list)),'o-')
    plt.xlabel('k')
    plt.ylabel('$\log_{10}(r_k)$')
    plt.title('Newton\'s Method Iteration --- x_k ')
    plt.legend(loc='upper right')
    plt.show()