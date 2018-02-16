d = "Multiply"
e = "Devide"
f = "Subtract"
g = "Add"
print("1 " + d)
print("2 " + e)
print("3 " + f)
print("4 " + g)
print
try:
    print("Choose an oparator")
    a = "-"
    b = "First number you want to "
    c = "Second number you want to "
    o = input()
    q = a * 99 
    if o == 1:
        print(b + d)
        r = input()
        print(c + d)
        k = input()
        print(q)
        print(r * k)
        print(q)
    if o == 2:
        print(b + e)
        r = input()
        print(c + e)
        k = input()
        print(q)
        print(r / k)
        print(q)
    if o == 3:
        print(b + f)    
        r = input()
        print(c + f)
        k = input()
        print(q)
        print(r - k)
        print(q) 
    if o == 4:                       
        print(b + g)
        r = input()
        print(c + g)
        k = input()
        print(q)
        print(r + k)
        print(q)
except ValueError:
    print("Error!")

