def f(x):
    return (x**2)

n = 10 #Aralık kaça bölünsün

x1 = 4
x2 = 7
h = (x2-x1)/n

#Kısa kenara göre integral
integral = 0
for i in range(n):
    integral += f(x1+i*h)*h
print("Kısa kenar=",integral)

#Uzun kenara göre integral
integral = 0
for i in range(1,n+1):
    integral += f(x1+i*h)*h
print("Uzun kenar=",integral)

#Orta Noktaya göre integral
integral = 0
for i in range(n):
    integral += f(x1+i*h+h/2)*h
print("Orta nokta=",integral)

integral = 0
for i in range(n):
    integral += (f(x1+i*h) + f(x1+(i+1)*h))*h/2
print("Yamuk alanı=",integral)

