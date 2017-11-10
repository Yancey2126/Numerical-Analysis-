import numpy as np
from matplotlib import pyplot as plt

tol = 1e-12  # If the "residual" |f(x_k)| < tol, stop iteration
printouts = True

def f(x):
    #return np.exp(x) - x - 2
    return x**2 - 2
    
def Illi(x0, x1):
    if x0 > x1:
        print 'Initial interval not exist!'

    if f(x0)*f(x1) > 0:
        print 'Same sign of interval ends!'

    else: 
        xkm1 = x0
        xk = x1
        xk_list = [xk]
        residual_list=[abs(f(xk))]    
        residual = abs(f(xk))

        while residual > tol:
            fkm1 = f(xkm1)
            # Define the iteration in Secant's fashion
            xkp1 = xk - ((xk - xkm1)/(f(xk) - fkm1))*f(xk)
            
            if f(xkp1) * f(xk) < 0:                     
                xkm1 = xk

            else: 
                fkm1 = 1/2 * f(xkm1)

            xk = xkp1
            fk = f(xk)
            residual = abs(fk)        

            if printouts:
                print xk, residual
            
            xk_list.append(xk)
            residual_list.append(residual)

    return xk_list, residual_list
    
xk_list, residual_list = Illi(1., 2.)
print 'Number of iterations = ', len(xk_list)

Plotting = True

if Plotting:
    fig = plt.figure(2)
    plt.plot(xk_list,'o')
    plt.xlabel('k')
    plt.ylabel('$x_k$')
    plt.title('Illinois\'s Method Iteration --- x_k ')
    plt.show()

    fig = plt.figure(3)
    plt.plot(np.log10(np.array(residual_list)),'o-')
    plt.xlabel('k')
    plt.ylabel('$\log_{10}(r_k)$')
    plt.title('Illinois\'s Method Iteration --- convergence rate')
    plt.show()