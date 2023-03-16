f=lambda x,y : (y**2) - y         #INPUT THE VALE OF "dy/dx" HERE
x,y= map(float, input("Enter initial value of x and y: ").split())
x1=float(input("Enter The Value of 'X' for which we have to calculte Y=??"))
n=int(input("Accuracy: "))
h=(x1-x)/n
for i in range(n):
    k1=h*f(x,y)
    k2=h*f(x+ h/2, y + k1/2)
    k3=h*f(x+ h/2, y + k2/2)
    k4=h*f(x+ h, y + k3)
    k=k1+ 2*k2+ 2*k3+ k4
    y=y+ k/6
    x=x+h
print(y)