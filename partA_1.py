#(i)
n = int(input("Enter number of elements : "))
print("Enter elements : ")
l = []
for i in range(n):
    temp = int(input())
    l.append(temp)
print("List :",l)

#(ii)
print("Minimum element :",min(l))
print("Maximum element :",max(l))

#(iii)
e = int(input("Enter the element to insert :"))
p = int(input("Enter the position to insert :"))
l.insert(p,e)
print("After insertion :",l)

#(iv)
e = int(input("Enter the element to delete :"))
l.remove(e)
print("After deletion :",l)

#(v)
e = int(input("Enter the element to find :"))
if e in l:
    print(e,"found in the list")
else:
    print(e,"not found in the list")