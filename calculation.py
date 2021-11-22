
# Necessary libraries for solution
from sympy.matrices import Matrix
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math

# Visualizing results
def heatmap2d(arr: np.ndarray):
    plt.imshow(arr, cmap='viridis', aspect='auto')
    plt.colorbar()
    plt.show()
 
# Defining the fuction and equation to be used for initial temperature 
def f(x, y):
    Ti = (q*y)/(k*A)+Tf
    return Ti

# Physical scenario is applied to a rectangle or cylinder
G=int(input('Rectangular(1) or Cylinder(2) '))
# rectangle equation
if G==1:
 
    #insert user defined parameters
    # material's conductivity
    k = float(input('k value '))
    # width of rectangle
    x = float(input('width of body '))
    # length of rectangle
    y = float(input('length of body '))
    # depth of rectangle
    z = float(input('depth of body '))
    # number of finite interpolation steps
    i = float(input('number of intervals per unit length '))
    # Hot temperature
    Ti = float(input('Thot '))
    # Cold temoerature
    Tf = float(input('Tcold '))
 
    # A is the surface area exposed to the heat
    A = z*x
    # interval equations
    # interval equation along x direction
    l=int((i*x)+1)
    # interval equation along y direction
    w=int((i*y)+1)

    # Heat flux (W/m^2) 
    q = k*A*(Ti -Tf)/y

    # input requested coordinates
    u = 1
    while u == 1:
        # length of rectangle 
        xi = float(input('x coordinate: '))
        # width of rectangle
        yi = float(input('y coordinate: '))
        
        #Temperature equation for fluid flow based on requested coordinates
        Tr = (Ti-((q*yi/(k*A))))
        # print value of temperature 
        print('This is the temperature for the location you requested:',Tr)
        # to calculation another temperature value for seperate initial temperature 
        o = input('Request another temperature?(Y/N)')
        if o == "Y":
            u = 1
        else:
            u = 0

    # defining the x and y area of the graph, the 3rd variable is no.elements=variable-1
    # using numpy to create grid points based on user specified iterations that rely on user specified length and width 
    # length coordinates  
    x = np.linspace(0, x, l)
    # width coordinates
    y = np.linspace(0, y, w)
    
    # using numpy .meshgrid to create a 2d matrix of grid points
    #creating the x and y data ranges
    X, Y = np.meshgrid(x, y)

    #defining the z axis
    # Z is for temperature values 
    Z = f(X, Y)
    
    # creating the graphical space
    # figure object for a plot 
    # create figure
    fig = plt.figure()
    
    # creating axes object for plot
    # add more than one axis to figure
    # projection creates a 3d plot
    ax = plt.axes(projection='3d')

    #creating the graph type and appearance
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='viridis',edgecolor='none')
    ax.plot_wireframe(X, Y, Z, color='black')

    #axix settings
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z');

# physical scenario for a hollow cyclinder    
else:
    #insert user defined parameters
    # distance from center (closest)
    ri = float(input('Inner Radius '))
    # distance from center (furthest)
    ro = float(input('Outer Radius '))
    # length of cyclinder
    L = float(input('Length of Cylinder '))
    # Temperature value closest to center
    Ti = float(input('Inner Temperature '))
    # Temperature value furthest from center
    To = float(input('Outer Temperature '))
    # Material's conductivity value
    k = float(input('k value '))
    # Number of intervals per unit length
    i = float(input('Number of intervals per unit length '))
    
    # Pi and Heat transfer of hollow cyclinder
    pi = math.pi
    q = 2*pi*L*k*((Ti-To)/np.log(ro/ri))
    
    # Print results
    #print('q = ' ,q)
    #print('To = ' ,Ti-(q*np.log(ro/ri))/(2*pi*L*k))

    #input requested coordinates
    u=1
    while u==1:
        rreq=float(input('Distance from ri: '))
        # equation for requested coordinates
        Tr=Ti-(q*np.log(rreq/ri))/(2*pi*L*k)
        print('This is the temperature for the location you requested:',Tr)
        o=input('Request another temperature?(Y/N)')
        if o=="Y":
            u=1
        else:
            u=0


    
    # Creates an array of data using np.arange of size () then reshapes into a matrix using .reshape of size (x (,:by) y)
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
