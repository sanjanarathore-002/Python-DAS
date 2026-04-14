num=int(input("enter a number :"));

if num%5==0 and num%11==0:
    print("number is divisible by 5 and 11");
elif num%2==0 and num%3==0:
    print("number is divisible by 2 and 3 ");
elif num%7==0 and num%13==0:
    print("number is divisible by 7 and 13 ");
else:
    print("number is not divisible by 5 and 11 or 2 and 3 or 7 and 13");