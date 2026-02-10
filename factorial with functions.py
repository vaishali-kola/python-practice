def factorial(n):
    fact=1
    while(n>1):
        fact=fact*n
        n=n-1
    return fact
num=int(input("enter a number"))
print(factorial(num))

    
