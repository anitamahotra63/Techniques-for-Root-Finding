#root finding using the technique of Newton Raphson

def f(x):
    return (x*x)-x-1;

def f_dash(x):
    return 2*x-1;

a=input("Enter the first number-: ");

m=a-(f(a)/f_dash(a));
fm=f(m);
i=0

if(fm>-0.0001 and fm<0.0001):
    print "root is ",m
    exit;
else:
    while(fm<-0.0001 or fm>0.0001):
        print "step-: ",i,"  a-: ",a,"  m-: ",m,"  f(m)-: ",fm;
        a=m;
        m=a-(f(a)/f_dash(a));
        fm=f(m);
        i=i+1;

print "root is ",m
