import numpy as np
from matplotlib import pyplot as plt

tol = 1e-12  # If the "residual" |f(x_k)| < tol, stop iteration
printouts = True

def f(x):
    #return np.exp(x) - x - 2
    #return x**2 - 2
    return np.sin(x**2) + 1.02 - np.exp(-x)
    

def Bisection(a0, b0):
    if a0 > b0:
        print 'Initial interval not exist!'
    
    if f(a0)*f(b0) > 0:
        print 'Same sign of interval ends'
        
    else:
        ak = a0
        bk = b0
        
        ak_list = [ak]
        bk_list = [bk]
        error_list = [abs(f(ak) - f(bk))]
        error = abs(f(ak) - f(bk))
        
        while error > tol:
            ck = (ak + bk)/2
            if f(ak)*f(ck) < 0:
                bk = ck
            else: 
                ak = ck
                
            error = abs(f(ak) - f(bk))
        
            if printouts:
                print ak, bk, error
        
            ak_list.append(ak)
            bk_list.append(bk)
            error_list.append(error) 
            
    return  ak_list, bk_list, error_list
    
    
ak_list, bk_list, error_list = Bisection(-0.5, 0.5)
print 'Number of iterations = ', len(ak_list)
    

Plotting = True

if Plotting:
    # Plot f(x)
    x = np.linspace(1. ,2. ,400)
    fig = plt.figure(1)
    plt.plot(x,f(x))
    plt.plot(x,np.zeros_like(x),'k-')
    plt.plot(np.array(ak_list),np.zeros(len(ak_list)),'o')
    plt.plot(np.array(bk_list),np.zeros(len(ak_list)),'o')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection\'s Method Iteration')
    plt.show()
    
    fig = plt.figure(2)
    plt.plot(ak_list,'o')
    plt.xlabel('k')
    plt.ylabel('$a_k$')
    plt.title('Bisection\'s Method Iteration --- x_k ')
    plt.show()

    fig = plt.figure(3)
    plt.plot(np.log10(np.array(error_list)),'o-')
    plt.xlabel('k')
    plt.ylabel('$\log_{10}(e_k)$')
    plt.title('Bisection\'s Method Iteration --- convergence rate')
    plt.show()