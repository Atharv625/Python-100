# Finally keyword
try:
    l=[1,5,6,7]
    i=int(input("enter index"))
    print(l[i])
except:
    print("outof the box")
finally:
    print("its done")