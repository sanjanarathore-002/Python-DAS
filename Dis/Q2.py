dt = {"rollno":120, "name":"sanju","marks":99};
# print(dt);
# print(len(dt));
# print(type(dt));
# print(dt.keys());
# print(dt.values());
# print(dt.get("rollno"));
# data=dt.items();
# print(data) 

print(dt);
dt["add"]="indore";
print(dt);
dt["rollno"]=102;
print(dt)
dt.pop("name");
print(dt);
