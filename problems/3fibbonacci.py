n= int(input("Enter the Number you want fibbonacci series: "))

a= 0
b=1
fibbo =[a,b]
for i in range(2,n):
    c = a + b
    a = b
    b = c 
    fibbo.append(c)
print("Fibonacci series till", n, "terms: ")
print(fibbo)
