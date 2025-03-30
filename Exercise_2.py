import time as t;
time=t.strftime("%H:%M:%S",t.localtime())
print(time)
m=t.strftime("%H",t.localtime())
if m<"00":
    print("Good Morning")
elif m<"12":    
    print("Good Afternoon")
else:
    print("Good Evening")