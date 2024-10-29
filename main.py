class student:
    __name = "ishan"
    n=9
    def __privfunc(self):
        print("I am accessible within the class only")
    def display(self):
        print("I am accessible outside the class only")
obj = student()
print(obj.n)
#print(obj.n) shows error because it is private#