import numpy as np
from matplotlib import pyplot as plt

tol = 1e-12  # If the "residual" |f(x_k)| < tol, stop iteration
printouts = True

def f(x):
    return np.sin(x**2) + 1.02 - np.exp(-x)
    
def Secant(x0, x1):
    # Two initial guesses
    xkm1 = x0
    xk = x1
    
    xk_list = [xk]
    residual_list=[abs(f(xk))]    
    residual = abs(f(xk))
    
    while residual > tol:    
        # Calculate the new xk by Secant's definition
        xkp1 = xk - ((xk - xkm1)/(f(xk) - f(xkm1)))*f(xk)
        
        # Update xkm1, xk and residual
        xkm1 = xk
        xk = xkp1
        
        residual = abs(f(xk))
        
        if printouts:
            print xk, residual
        
        # Add new iteration results into the list
        xk_list.append(xk)
        residual_list.append(residual)
        
        if len(xk_list)==200:
            print 'Did not converge after 200 iterations'
            break

    return xk_list, residual_list
    
xk_list, residual_list = Secant(0.9, 1.)
print 'Number of iterations(Secant) = ', len(xk_list)

Plotting = True

if Plotting:
    # Plot f(x)
    x = np.linspace(1. ,2. ,400)
    fig = plt.figure(1)
    plt.plot(x,f(x))
    plt.plot(x,np.zeros_like(x),'k-')
    plt.plot(np.array(xk_list),f(np.array(xk_list)),'o')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Secant\'s VS Newton\'s Method Iteration')
    plt.show()
    
    fig = plt.figure(1)
    plt.plot(xk_list,'o')
    plt.xlabel('k')
    plt.ylabel('$x_k$')
    plt.title('Secant\'s VS Newton\'s Method Iteration --- x_k ')
    plt.show()

    fig = plt.figure(2)
    plt.plot(np.log10(np.array(residual_list)),'o-')
    plt.xlabel('k')
    plt.ylabel('$\log_{10}(r_k)$')
    plt.title('Secant\'s VS Newton\'s Method Iteration --- convergence rate')
    plt.show()