print("Right angle triangle pattern")
for i in range(1,6):
    print("#" * i)


print()
print("inverted right angle triangle pattern")
for i in range(5,0,-1):
    print("#" * i)

print()
print("Right Angle Triangle(Number Pattern)")
for i in range(1,6):
    print(' '.join(str(x) for x in range(1,i+1)));

print()
print("Inverted right angle tringle(number pattern)")
for i in range(5,0,-1):
    print(' '.join(str(x) for x in range(1, i+1)))

print()
print("join ");
for i in range(1,6):
    print(' '.join(str(x) for x in range(1,i+1)))
for i in range(6,0,-1):
    print(' '.join(str(x) for x in range(1,i+1)))  

print()
print("Hollow right angle triangle")
for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or j==i or i==5:
            print("*",end='')
        else:
            print(' ',end='')
    print()