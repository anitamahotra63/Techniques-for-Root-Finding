#Root finding using the method of Bisection

def f(x):
    return (x*x)-x-1;

a=input("Enter first point of interval-: ")  #starting point of interval
b=input("Enter second point of interval-: ") #end point of interval


if(f(a)*f(b)>0):
    #checking if both interval points lie on same side or not
    print "invalid interval..better luck next time."
else:
    m=(a+b)/2
    fm=f(m)
    if(fm>-0.0001 and fm<0.0001):
        print "root is ",m
        exit
    else:
        while(f(m)<-0.0001 or f(m)>0.0001):
            print "a-: ",a,"  b-: ",b,"  m-: ",m,"  f(m)-: ",m;
            if(f(a)*f(m)>0):
                a=m
            else:
                b=m
            m=(a+b)/2
        
    print "root is-: ",m
