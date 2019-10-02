def addition(a,b):
    print("addition",a+b)
def primernot(n):
    fact=0
    for i in range(1,n+1):
        if(n%i==0):
            fact=fact+1
    if(fact==2):
        print("true")
    else:
        print("false")  