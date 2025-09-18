print("pyramid pattern")
for i in range(1,6):
    print(" " * (5-i)+"#" *(2*i-1))

print()
print("Inverted pyramid pattern")
for i in range(5,0,-1):
    print(" "*(5-i)+"*" * (2*i-1))

print()
print("Hollow pyramid pattern")
for i in range(1,6):
    for j in range(5-i):
        print(' ',end='')
    for j in range(2*i-1):
        if j==0 or j==2 * i - 2 or i==5:
            print("*",end='');
           
        else:
            print(' ',end='')
    print()