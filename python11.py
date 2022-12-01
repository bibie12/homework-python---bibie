# (11) ha har sa lia
def sum(number):
    total,avg = 0,0
    for i in number :
        total+=i
    avg = total/len(number)
    return total,avg


x=[1,2,3,4,5,6]
y,z = sum(x)
print(y)
print(z)
