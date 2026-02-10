def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        rev=rev*10+n%10
        n=n//10
    if(temp==rev):
        return "palindrome"
    else:
        return "not a palindrome"
num=int(input("enter a number"))
print(palindrome(num))
        







num=int(input("enter a number"))
print(palindrome(num))
    
