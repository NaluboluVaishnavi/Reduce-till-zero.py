#48 18 
#6
x = int(input())
y = int(input())
while y>0:
    if x<y:
        temp = x
        x = y
        y = temp
        #x,y = y,x
    t = x-y
    x = y
    y = t
print(x)

