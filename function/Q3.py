# def hello():
#     print("Hello, World!");
#     hello();
# hello();

#1-10 print kar hai
count=0;
def number():
    global count;
    count=count+1;
    if count<=10:
        print(count);
        number();
    
    
number();
