class student:
    def __init__(self,name,age,marks):
        self.n = name
        self.a = age
        self.m = marks

    def display(self):
        print("Name :",self.n)
        print("Age :",self.a)
        print("Marks :",self.m)
    
    def update(self):
        self.n = input("Enter name : ")
        self.a = int(input("Enter age : "))
        l = []
        for i in range(3):
            print("Enter marks",(i+1)," :")
            temp = int(input())
            l.append(temp)
        self.m = l


s1 = student("Raju",20,[20,30,40])
print("Student 1 information")
s1.display()
s2 = student("X",0,0)
print("Enter student 2 information")
s2.update()
print("Student 2 information")
s2.display()