str1="this is a string";
#Case conversion
print(str1.upper());
print(str1.lower());
print(str1.title());
print(str1.capitalize())
print(str1.swapcase());


#searching & Finding
text= "this is a Python class";
print(text.find("Python"));
print(text.rfind("is"));
print(text.index("class"));
print(text.rindex("is"));
print(text.count("s"));
print(text.startswith("this"));
print(text.endswith("class"));

# checking the presence of a substring
print("Python" in text);
print(text.isalnum());
print("hellojikeseho".isalpha());
print("123456".isdigit());
print("   ".isspace());
print("hello world".isspace());
print("hello world".isupper());
print("HELLO WORLD".isupper());
print("hello world".islower());
print("HELLO WORLD".islower());
print("hello world".istitle());
print("Hello World".istitle());
print("hello world".isprintable());
print("hello\nworld".isprintable());


# Trimming & Stripping
str2="   hello world   ";
print(str2.strip());
print(str2.lstrip());
print(str2.rstrip());


#Splitting & Joining
str3="hello coding world !";
print(str3.replace("coding","java"));
print(str3.split());
print(str3.split("o"));
print("a-b-c".rsplit("-", 1));
print("-".join(["a","b","c"]));

#String formatting
name='rajaram rathore';
age=100;
print("My name is {} and I am {} years old.".format(name, age));
print("My name is {0} and I am {1} years old.".format(name,age));
