str="sanjana"; #sanjana =anajnas
last=" "
for ch in str:
    last=ch+last
print(last)

print(1234/10)

num=int(input("enter a number :"))
reversed_num =0
while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

print(reversed_num)