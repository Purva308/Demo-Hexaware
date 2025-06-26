'''
l=[1,2,3,4,5,6]
print(l[1])
print(l[::-1])
print(l[-3])
for item in l:
    print(item+2,end=" ")
print(" ")
print(l*3)
print(dir(l))

l.append(100)
print(l)
l.insert(2,130)
print(l)
print(l.count(100))
l.remove(130)
print(l)
print(l.index(2))


n=int(input("Enter the number:"))
if n % 2 == 0:
    print(f"The number {n} is even.")
else:
    print(f"The number {n} is odd.")
   '''




