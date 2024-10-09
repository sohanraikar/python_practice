n=int(input())
if n%2==1:
    print("WEIRD")
elif n%2==0:
    if 2<=n<=5:
        print("NOT WEIRD")
    elif 6<=n <=20:
        print("WEIRD")
    elif n>20:
        print("NOT WEIRD")
        
