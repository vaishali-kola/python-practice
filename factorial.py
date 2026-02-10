num=int(input("enter number of terms:"))
a=0
b=1
count=0
while(count<num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    count=count+1

    
