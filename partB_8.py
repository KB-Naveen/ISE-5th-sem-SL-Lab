class rev:
    def __init__(self,sentense):
        self.s = sentense

    def reverse(self):
        self.s = self.s.split()
        self.s.reverse()
        return " ".join(self.s)

o = ['a','A','e','E','i','I','o','O','u','U']
s_list = []

for i in range(3):
    print("Enter sentense",(i+1),": ",end='')
    s = input()
    n = sum([list(s).count(owel) for owel in o])
    s_list.append((n,s))

s_list = sorted(s_list,reverse=True)

for i in range(3):
    obj = rev(s_list[i][1])
    print("reversed sentense",(i+1),":",obj.reverse())