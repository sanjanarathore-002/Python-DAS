# print("Butterfly Pattern");
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ");
#     for j in range(1,2 * (5-i)):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

n=5
# Upper Half
for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    for j in range(1, 2*(n-i)+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()

# Lower Half
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    for j in range(1, 2*(n-i)+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()