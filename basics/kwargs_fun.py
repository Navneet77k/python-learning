def student (**kwargs):
    return kwargs
x=student(name="NAVNEET" , AGE = 22, branch="cse")
print(x)

# or 

def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="NAVNEET", age=22, branch="CSE")