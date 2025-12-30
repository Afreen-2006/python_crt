'''fibonacci using method'''

def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
n=int(input())
fib(n)
'''using recurrsion'''

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
n=int(input())
print(fib(n))
'''factorial using method'''
def fact(n):
    f=1
    for i in range(1,n+1):
     f*=i
     print(f)
fact(5)

'''factorial using recurrsion'''
def facti(n):
    if n==0 or n==1:
        return n
    return n*facti(n-1)
print(facti(6))
