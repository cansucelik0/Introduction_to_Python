def squaring(x):
  print("Entered number: " + str(x) + " Square of the entered number: " + str(x**2))
squaring(3)


def mul_1(x, y=1):
    print(x*y)  
mul_1(2,3)    


#Incorrect:
def direct_calculus(heat, moisture, charge):
     print((heat+moisture)/charge)
direct_calculus(25,40,70)*9


#Adding return solves the problem.
def direct_calculus(heat, moisture, charge):
    return (heat+moisture)/charge
direct_calculus(25,40,70)*9


#Local and global variables

#Global:
x = 10
y = 20

#Local
def mul_2(x,y):
    return x*y

mul_2(2,3)

#Local Global Examples
x=[]
def add_value(y):
    x.append(y)
    print(str(y)+"statement added")
add_value("ali")
add_value("veli")