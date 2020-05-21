#print Fibonacci series unto nth number

num= int(input("Enter the value of N: "))
a = 0
b = 1
print("The Fibonacci series of",num,"number :-")
for i in range(num):
    print(a, end = " ")
    c = a + b
    a = b
    b = c
