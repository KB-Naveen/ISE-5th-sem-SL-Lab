from functools import reduce
l = [1,2,3,4,5,6]
print("Original List :",l)
new_l = [3*x for x in l]
print("New List :",new_l)

s = reduce(lambda a,b:a+b, l)
print("Original List sum :",s)
new_s = reduce(lambda a,b:a+b, new_l)
print("New List sum :",new_s)