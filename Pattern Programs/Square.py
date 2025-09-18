print("Square Pattern");
print("Hollow square Pattern");
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end="")
        else:
            print(" ", end="")

    print()

print()
print("Full square pattern")
for i in range(5):
    print("*" * 5)
