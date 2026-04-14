first=int(input("enter a first number "));
second=int(input("enter a second number"));
third =int(input("enter a third number "));

if first>second and first>third:
    print("first number is largest");
elif second>first and second>third:
    print("second number is largest ");
elif third>first and third >second:
    print("thirs number is largest ");
else:
    print("every number is equal");