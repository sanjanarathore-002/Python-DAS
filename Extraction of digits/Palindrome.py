# # n=12234;
# n=int(input("enter a number :"))
# num=n;
# result=0;
# while num>0:
#     Iastdigit=num%10
#     result=(result*10)+Iastdigit
#     num=num//10
# if n==result:
#         print("this a palindrome number")
# else:
#         print("this not a palindrome number")   


user_input = input("Enter a number or string: ")

# Case 1: If input is digits → treat as number
if user_input.isdigit():
    num = int(user_input)
    original = num
    reversed_num = 0

    # reverse the number
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    if original == reversed_num:
        print("It is a palindrome number.")
    else:
        print("It is not a palindrome number.")

# Case 2: Otherwise → treat as string
else:
    if user_input == user_input[::-1]:
        print("It is a palindrome string.")
    else:
        print("It is not a palindrome string.")


print("123".isdigit())     # True  (all are digits)
print("42a".isdigit())     # False (because of 'a')
print("".isdigit())        # False (empty string)
print("-123".isdigit())    # False (because of '-')
