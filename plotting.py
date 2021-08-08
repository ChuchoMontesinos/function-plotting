"""
Program that plots a function according with its characteristics 
"""
# Importing the libraries
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Declaring the symbols to be used, these are real
x, y, z, t = sp.symbols("x y z t", real=True)

# Asking for the kind of function to be plot
print("Program that plots a function\n")
op = int(input("Select 1. f(x), 2. f(x,y), 3. f(x(t), y(t)), 4. f(x(t),y(t),z(t)): "))

"""
Entering to the flow of the program according with the option "op"
"""
if(op == 1):
    # Here we plot the function f: R->R
    fRR = input("Write the function f(x): R->R:  ")  # Asking for the function
    exprfRR = sp.sympify(fRR)  # Turning into a SymPy expression
    # Lambdifiying the function to be evaluated
    lamexprfRR = sp.lambdify(x, exprfRR, 'numpy')
    # Asking for the interval (a,b)
    print("Please write the domain of the function (a,b)")
    a0 = float(input("Point 'a':   "))
    b0 = float(input("Point 'b':   "))
    X = np.arange(a0, b0, 0.1)  # Range of f
    Y = lamexprfRR(X)  # Evaluating the points
    plt.plot(X, Y)  # Plotting
    plt.title("Plot of %s" % (exprfRR))
    plt.xlabel("x")
    plt.ylabel("%s" % (exprfRR))
    plt.show()

if(op == 2):
    # Here we plot the function f:R2->R
    # Asking for the function
    fR2R = input("Write the function f(x,y): R2->R:   ")
    exprfR2R = sp.sympify(fR2R)  # Turning into a SymPy expression
    # Lamdifying the function to be evaluated
    lamexprfR2R = sp.lambdify((x, y), exprfR2R, 'numpy')
    # Asking for the interval (a,b) in the X axis
    print("Please write the domain of the function (a,b) for x's")
    a0 = float(input("Point 'a':   "))
    b0 = float(input("Point 'b':   "))
    print("Please write the domain of the function (c,d) for y's")
    c0 = float(input("Point 'c':   "))
    d0 = float(input("Point 'd':   "))
    X, Y = np.meshgrid(np.arange(a0, b0, 0.1),
                       np.arange(c0, d0, 0.1))  # Creating the mesh
    Z = lamexprfR2R(X, Y)  # Declaring the function
    # Plotting the function
    ax = plt.axes(projection="3d")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("%s" % (exprfR2R))
    ax.plot_surface(X, Y, Z)
    plt.show()

if(op == 3):
    # Here we plot the function f(x(t),y(t)): I->R2
    # Asking for the function
    fIRx = input("Write the function x(t):   ")
    fIRy = input("Write the function y(t):   ")
    # Sympifying and lambdifying the functions
    exprfIRx = sp.sympify(fIRx)
    exprfIRy = sp.sympify(fIRy)
    lamexprfIRx = sp.lambdify(t, exprfIRx, 'numpy')
    lamexprfIRy = sp.lambdify(t, exprfIRy, 'numpy')
    # Asking for the interval (a,b)
    print("Please write the domain of the function (a,b)")
    a0 = float(input("Point 'a':   "))
    b0 = float(input("Point 'b':   "))
    # Plotting
    points = np.arange(a0, b0, 0.1)
    X = lamexprfIRx(points)
    Y = lamexprfIRy(points)
    plt.plot(X, Y)
    plt.title("Plot of (%s,%s)" % (exprfIRx, exprfIRy))
    plt.legend()
    plt.show()

if(op == 4):
    # Here we plot the function f(x(t)): I->R3
    # Asking for x(t), y(t), z(t)
    fIR3x = input("Write the function x(t):   ")
    fIR3y = input("Write the function y(t):   ")
    fIR3z = input("Write the function z(t):   ")
    # Sympyfying  and lambdifying the functions
    exprfIR3x = sp.sympify(fIR3x)
    exprfIR3y = sp.sympify(fIR3y)
    exprfIR3z = sp.sympify(fIR3z)
    lamexprfIR3x = sp.lambdify(t, exprfIR3x, 'numpy')
    lamexprfIR3y = sp.lambdify(t, exprfIR3y, 'numpy')
    lamexprfIR3z = sp.lambdify(t, exprfIR3z, 'numpy')
    # Asking for the interval (a,b)
    print("Please write the domain of the function (a,b)")
    a0 = float(input("Point 'a':   "))
    b0 = float(input("Point 'b':   "))
    # Creating the range of the function
    points = np.arange(a0, b0, 0.1)
    # plotting
    X = lamexprfIR3x(points)
    Y = lamexprfIR3y(points)
    Z = lamexprfIR3z(points)
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(X, Y, Z)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    plt.title("Plot of (%s,%s,%s)" % (exprfIR3x, exprfIR3y, exprfIR3z))
    plt.show()
