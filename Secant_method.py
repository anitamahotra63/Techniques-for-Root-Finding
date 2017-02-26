#root finding using the technique of secant method

def f(x):
    return (x*x)-x-1;

a=input("enter the first point of interval-:")
b=input("enter the second point of interval-:")

fa=f(a)
fb=f(b)
m=(a*fb-b*fa)/(fb-fa)
fm=f(m)

if(fm>-0.0001 and fm<0.0001):
    print "root is-:",m
    exit
else:
    while(fm<-0.0001 or fm>0.0001):
        print "a-: ",b,"  b-: ",b,"  m-: ",m," f(m)-:",fm
        a=b;
        b=m;
        fa=f(a)
        fb=f(b)
        m=(a*fb-b*fa)/(fb-fa)
        fm=f(m)

print "root is-:",m
