def mensaje(b):
    r=b+b
    return r

def sumar(a,b):
    r=a+b
    return r

def cuadrado(x):
    res=x**2
    return res

def raiz(x):
    rd=x**0.5
    return rd

def par(x):
    if(x%2==0):
        b=True
    else:
        b=False
    return b

def varios(a,b,c=1):
    suma=a+b
    resta=a-b
    mul=a*b
    div=a/b
    return suma,resta,mul,div

#promedio de 3 numeros
def promedio(a,b,c):
    rdo=(a+b+c)/3
    return rdo

#número es primo
def esPrimo(n):
    con=0
    for i in range(2,n):
        if(n%i==0):
            con=con+1
    if(con>=1):
        return False
    else:
        return True

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

