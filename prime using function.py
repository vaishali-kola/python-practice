def prime(n):
    if(n==2):
        return "prime"
    elif(n<=1):
        return "not a prime"
    elif(n%2==0):
        return "not a prime"
    
num=int(input("enter a number:"))
print(prime(num))