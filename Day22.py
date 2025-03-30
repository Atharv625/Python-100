# it's about List Datatype

l=[1, 2, 3, 4, 5,True, "Hello", 3.14, [1, 2, 3], (1, 2), {1: "one", 2: "two"}, {1, 2, 3}]
print(l[0])  # 1
print(l)
print(type(l))  # <class 'list'>
print(len(l))  # 5
if(4 in l):
    print("4 is in the list")
else:
    print("4 is not in the list")
print(l)
list=[i for i in range(1, 11)]
print(list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]