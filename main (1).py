'''' right angle hallow'''
x=int(input())
for i in range(x):
    for j in range(i+1):
        if i==j or j==0 or i==x-1 or j==x-1:
             print("*",end="")
        else:
            print("",end=" ")
    print()
 
  