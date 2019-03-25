def f(x):
    return (x**2-4*x+3)

x1 = int(input("Başlangıç tahminini giriniz: "))
x2 = int(input("Bitiş tahminini giriniz: "))
delta = 0.001
temp = -100000

if(f(x1)*f(x2) == 0):
    print("Tahminlerden biri denklem kökü.")
elif(f(x1)*f(x2) > 0):
    print("Bu aralıkta tek sayida kök yok.")
else:
  
    while True:   
        xr = (x2*f(x1) - x1*f(x2)) / (f(x1)-f(x2))
        if(f(xr) == 0):
            print("denklemin kökü=",xr)
            break
        elif(f(x1)*f(xr) < 0):
            temp = x2
            x2 = xr
        else:
            temp = x1
            x1 = xr
        if(abs(xr-temp) < delta):
            print("Denklemin kökü=",xr)
            break

