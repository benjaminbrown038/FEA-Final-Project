# include corresponding units (normalizing the data) for user's inputs 

'''
This script will run in a terminal.

parameters: <int> 1 or 2. Integers specify geometry (rectangle or cylinder) of heat problem (equations)
            
            1 
                parameters: <int> Material's conductivity
                            <int> width
                            <int> length
                            <int> depth
                            <int> number of intervals 
                            <int> Initial Temperature (cold)
                            <int> Final Temperature (heat)
                            <int> specific x-coordinate for requested temperature 
                            <int> specific y-coordinate for requested temperature 
                
                returns:    <int> Temperature value for requested location
               
            2 
                parameters: <int> inner radius 
                            <int> outer radius 
                            <int> length 
                            <int> outer temperature
                            <int> material's conductivity (how well it retains heat)
                            <int> number of intervals
                 
                 returns:   <int> Temperature value for requested location
               
                   
            
returns: <int> Temperature value for requested location
'''

import numpy as np
import matplotlib.pyplot as plt
import math
import mpl_toolkits

'''
Function for visualizing the results of temperature values with respect to 2d conditions of geometry
'''
# Visualizing results
def heatmap2d(arr: np.ndarray):
    plt.imshow(arr, cmap='viridis', aspect='auto')
    plt.colorbar()
    plt.show()
    
'''
Function for determining temperature within for rectangle after grid points are added for visualizing
'''
# Defining the fuction and equation to be used for initial temperature 
def f(x, y):
    Ti = (q*y)/(k*A)+Tf
    return Ti

# Physical scenario is applied to a rectangle or cylinder
G = int(input('Rectangular(1) or Cylinder(2): '))

'''
Rectangular Conditions:

parameters: <int> Material's conductivity
            <int> width
            <int> length
            <int> depth
            <int> number of intervals 
            <int> Initial Temperature (cold)
            <int> Final Temperature (heat)
            <int> specific x-coordinate for requested temperature 
            <int> specific y-coordinate for requested temperature 
                
returns:    <int> Temperature value for requested location

'''

'''
Gathering user inputs (rectangular data)
'''
if G == 1:
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
 
'''
Calculating temperature values based on user inputs
'''
    # A is the surface area exposed to the heat
    A = z*x
    # interval equations
    # interval equation along x direction
    l = int((i*x)+1)
    # interval equation along y direction
    w = int((i*y)+1)

    # Heat flux (W/m^2) 
    q = k*A*(Ti -Tf)/y
    # creating truth condition
    u = 1

'''
Calculating temperature for specific locations based on user inputs
'''
    # input requested coordinates
    while u = 1:
        # length of rectangle 
        xi = float(input('x coordinate for temperature within body: '))
        # width of rectangle
        yi = float(input('y coordinate for temperature within body: '))
        # Temperature equation for fluid flow based on requested coordinates
        Tr = (Ti-((q*yi/(k*A))))
        # print value of temperature 
        print('This is the temperature for the location you requested:',Tr)
        # to calculation another temperature value for seperate initial temperature 
'''
Asking user if another temperature value is needed
'''
        o = input('Request another temperature?(Y/N)')
        if o == "Y":
            u = 1
        else:
            u = 0

'''
Plotting results based on rectangular physics problem
'''
    # defining the x and y area of the graph, the 3rd variable is no.elements=variable-1
    # using numpy to create grid points based on user specified iterations that rely on user specified length and width 
    # length coordinates  
    x = np.linspace(0, x, l)
    # width coordinates
    y = np.linspace(0, y, w)
    # using numpy .meshgrid to create a 2d matrix of grid points
    # creating the x and y data ranges
    X, Y = np.meshgrid(x, y)
    # defining the z axis
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
    # axis settings
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('Temperature');
    
    
'''    
Conditions for a Cylindrical geometry for finding temperature (fluids-heat) values.

parameters: <int> inner radius 
            <int> outer radius 
            <int> length 
            <int> outer temperature
            <int> material's conductivity (how well it retains heat)
            <int> number of intervals
                 
returns:   <int> Temperature value for requested location

'''

'''
Gathering Cylindrical data 
'''
# physical scenario for a hollow cyclinder    
else:
    # insert user defined parameters
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
    
    # Heat transfer for a hollow cylinder based on above (user input) values
    q = 2*pi*L*k*((Ti-To)/np.log(ro/ri))
    
    # Print results
    # print('q = ' ,q)
    # print('To = ' ,Ti-(q*np.log(ro/ri))/(2*pi*L*k))

    # creating truth condition
    u = 1
    
'''
Asking user to specify the coordinates for which they want to know the temperature. 

This is after temperature values are known among all grid points. 

'''
    while u == 1:
        # the distance (from center) at which we will calculate temperature 
        rreq = float(input('Distance from ri: '))
        # temperature for requested location
        Tr = Ti-(q*np.log(rreq/ri))/(2*pi*L*k)
        # show user the temperature for the distance from center of hollow cylinder
        print('This is the temperature for the location you requested:',Tr)
            
'''
Option for additional values within coordinates
'''
        # Another temperature value 
        o = input('Request another temperature?(Y/N)')
        if o == "Y":
            u = 1
        else:
            u = 0

'''
1. Calculating temperature values along cylindrical grid points 
2. Append to a list 
'''
    while r <= ro:
        # calculating temperature based on Fourrier's equation
        T = Ti-(q*np.log(r/ri))/(2*pi*L*k)
        # append temperature values to list to mimick temperature values on 2d surface
        Tlist.append(T)
        # updating r values 
        r = r+(1/i)
    
'''
1. Store results in an array 
2. Append to a matrix
3. Visualize matrix
'''
    # Creates an array of data using np.arange of size () then reshapes into a matrix using .reshape of size (x (,:by) y)
    r = ri
    Tlist = []
    # creating an array of temperature values 
    Tarray =  np.array(Tlist)
    # reshaping the array of temperature values into 
    # size of interval range to create matrix depending number of iterations on one unit length 
    size = int(i*(ro-ri)+1)
    Tmatrix = Tarray.reshape(1,size)
    # Display results using function at top of script
    heatmap2d(Tmatrix)
