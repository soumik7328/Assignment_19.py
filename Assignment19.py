#1. Write a python program to create a simple function which prints “MySirG” .
def saurabh():
    print("MySirG")
saurabh()    
#2. Write a python program to create a function which expects two arguments and print them in the function body.
def num(a,b):
    print(a,b)
num(4,5)   
#3. Write a python program to create a function which expects an unknown number of arguments.
def func(a,b):
    print (a,b)

args=(1,2)
func(*args)
#4. Write a python program to create a function which expects kwargs arguments.
def info(**data):
    print("\nData type of argument:",type(data))     

    for key, value in data.items():
        print("{} is {}".format(key,value))

info(Firstname="Soumik", Lastname="Ghosh", Age=16, Class=11)
#5. Write a python program to create a function which expects a list as an argument.
def lst(car):
    for x in car:
        print(x, end=' ')
bike=['Ktm350','BMWs1000rr','R15','Hayabusa']
lst(bike)        
#6. Write a python program to create a function that finds a maximum of four numbers.
def maximum():
    print("\nEnter 4 number:-")
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    print("Maximum number is=",max(a,b,c,d))
    
maximum()
#7. Write a python program to sum all the numbers in a list.
def lst1(abd):
    sum=0
    for x in abd:
        sum=sum+x
    return sum   
l1=(input("Enter some number in list. with coma shepareted:- "))
l2=l1.split(',')
for i in range(len(l2)):
    l2[i]=int(l2[i])
print("sum of elements in a given list of numbers=",lst1(l2))
#8. Write a python program to multiply all the numbers in a list.
def lst1(abd):
    sum=1
    for x in abd:
        sum=sum*x
    return sum   
l1=(input("Enter some number in list. with coma shepareted:- "))
l2=l1.split(',')
for i in range(len(l2)):
    l2[i]=int(l2[i])
print("multiply all the numbers in a lists=",lst1(l2))
#9. Write a python program to create a function to check whether a number falls in a given range.
def t_range(n):
    if n in range(0,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
t_range(5)

#10. Write a python program to create a function to check whether a given number is even or odd.
def check(input1):
    if input1%2==0:
        print("Even number")
    else:
        print("odd number")

input2=float(input("Enter a number:-"))
check(input2)

