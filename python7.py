# (7) pien na t pen sua m
print("Enter times:")
value = int(input())
if value >= 60:
    time = value // 60
    print(time, "h:", value % 60, "mn")
else:
    print("0 h:", value % 60, "mn")  