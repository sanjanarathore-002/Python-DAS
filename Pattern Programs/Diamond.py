
print("Diamond Pattern")
for i in range(1,6):
    print(' ' * (5-i) + "*" * (2*i-1))
for i in range(4,0,-1):
    print(" "*(5-i)+ "*"*(2*i-1))

print()
print("Hollow Diamond Pattern")
# n=5
# for i in range(1,n+1):
#     print(" "*(n-i) + "*"+" "*(2*i-3)+("*" if i > 1 else ""))
# for i in range(n-1 ,0 ,-1):
#     print(" "*(n-i) + "*"+" "*(2*i-3)+("*" if i > 1 else ""))


n = 5
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + ('*' if i > 1 else ''))

print();
print("Hollow Diamond (Number Pattern)")

num = 5
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(' ', end='')
    for j in range(1, 2 * i):
        if j == 1 or j == 2 * i - 1:
            print(i, end='')
        else:
            print(' ', end='')

    print()

