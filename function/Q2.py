def add(a,b):
    global x;
    x=a;
    global y;
    y=b;
    global add;
    add=a+b;

add(10,20);
print("a=",x);
print("b=",y);
print("c=",add);