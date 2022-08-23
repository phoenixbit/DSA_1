import math

x = float(input("Please input the first integer : "))
y = float(input("Please input the second integer : "))
z = float(input("Please input the third integer : "))
# -b+- -/b^2-4ac/2a

D = math.sqrt(math.pow(y, 2) - (4 * x * z))
if D>0:
    root_1 = ((-y) + D) / (2 * x)
    root_2 = ((-y) - D) / (2 * x)
    print("The roots are : " + str(root_1) + ", " + str(root_2))
else:
    real_p = (-y)/2*x
    imag_p = math.sqrt(-D)/2*x
    print("The real and imaginary parts are as follows : " + str(real_p) + str(imag_p))


