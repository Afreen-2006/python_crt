'''square hallow pattern'''

x=int(input())
for i in range(x):
    for j in range(x):
        print("",end=" ")
        if i==0 or j==0 or i==x-1 or j==x-1:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
  
  