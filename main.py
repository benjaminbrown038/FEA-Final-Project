
G=int(input('Rectangular(1) or Cylinder(2) '))
if G==1:
    #completed rectangular code
    # install sympy 
 
    from sympy.matrices import Matrix
 

    #insert user defined parameters
    k = float(input('k value '))
    x = float(input('width of body '))
    y = float(input('length of body '))
    z = float(input('depth of body '))
    i = float(input('number of intervals per unit length '))
    Ti = float(input('Thot '))
    Tf = float(input('Tcold '))
 

    # A is the surface area exposed to the heat
    A = z*x
    #interval equations
    l=int((i*x)+1)
    w=int((i*y)+1)
 

    #Calculate the heat transfer q
    q = k*A*(Ti -Tf)/y
    #print('q = ' ,q)
    #print('Ti = ' ,((q*y)/(k*A))+Tf)



 #input requested coordinates
    u=1
    while u==1:
        xi=float(input('x coordinate: '))
        yi=float(input('y coordinate: '))
        #equation for requested coordinates
        Tr=(Ti-((q*yi/(k*A))))
        print('This is the temperature for the location you requested:',Tr)
        o=input('Request another temperature?(Y/N)')
        if o=="Y":
            u=1
        else:
            u=0

    #importing matplotlib for graph
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt

    #defining the fuction and equation to be used
    def f(x, y):
        return (q*y)/(k*A)+Tf

    #defining the x and y area of the graph, the 3rd variable is no.elements=variable-1
    x = np.linspace(0, x, l)
    y = np.linspace(0, y, w)

    #creating the x and y data ranges
    X, Y = np.meshgrid(x, y)

    #defining the z axis
    Z = f(X, Y)
    #creating the graphical space
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    #creating the graph type and appearance
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')
    ax.plot_wireframe(X, Y, Z, color='black')

    #axix settings
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z');
else:
    #finished cylinder code
    #insert user defined parameters
    ri = float(input('Inner Radius '))
    ro = float(input('Outer Radius '))
    L = float(input('Length of Cylinder '))
    Ti = float(input('Inner Temperature '))
    To = float(input('Outer Temperature '))
    k = float(input('k value '))
    i = float(input('number of intervals per unit length '))


    #Calculate the heat transfer q
    import numpy as np
    import math


    pi = math.pi
    q = 2*pi*L*k*((Ti-To)/np.log(ro/ri))
    print('q = ' ,q)
    #print('To = ' ,Ti-(q*np.log(ro/ri))/(2*pi*L*k))


    #input requested coordinates
    u=1
    while u==1:
        rreq=float(input('Distance from ri: '))
        #equation for requested coordinates
        Tr=Ti-(q*np.log(rreq/ri))/(2*pi*L*k)
        print('This is the temperature for the location you requested:',Tr)
        o=input('Request another temperature?(Y/N)')
        if o=="Y":
            u=1
        else:
            u=0
        

    import matplotlib.pyplot as plt
    import numpy as np


 def heatmap2d(arr: np.ndarray):
        plt.imshow(arr, cmap='viridis', aspect='auto')
        plt.colorbar()
        plt.show()
    #creates an array of data using np.arange of size () then reshapes into a matrix using .reshape of size (x (,:by) y)
    r=ri
    size=int(i*(ro-ri)+1)

    Tlist = []

    while r <= ro:
        T = Ti-(q*np.log(r/ri))/(2*pi*L*k)
        Tlist.append(T)
        r=r+(1/i)
    

    Tarray =  np.array(Tlist)
    Tmatrix = Tarray.reshape(1,size)
    #print(Tmatrix)
    heatmap2d(Tmatrix)
