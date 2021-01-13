#(a)
l = [1,2,3,1,4,8,3,4]
def deldup(li):
    new_l = []
    for i in li:
        if(i not in new_l):
            new_l.append(i)
    return new_l
print("Original list :",l)
print("Without duplicate :",deldup(l))

even_list = [2*x for x in range(10)]
print("List of ten even numbers :",even_list)

even_list.reverse()
print("Reversed list :",even_list)

#(b)
from collections import Counter

word_freq = Counter(open('sample.txt').read().split())
print("Word frequency in the file :",word_freq)

#(c)
l = [1,2,3,1,4,8,3,4]
def maximum(li,n):
    if(n==1):
        print("Maximum value :",li[0])
        return
    else:
        li.remove(min(li))
        maximum(li,len(li))

maximum(l,len(l))