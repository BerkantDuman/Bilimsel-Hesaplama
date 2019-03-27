def f(x):
    return(x**2+4*x+3)

x1 = int(input("Başlangıç değerini giriniz= "))
x2 = int(input("Bitiş değerini giriniz= "))

for i in range(10):
    x3 = x1-f(x1)*(x2-x1)/(f(x2)-f(x1))
    x1,x2 = x2,x3
    if(x1==x2):
        break
print(x1,x2)
