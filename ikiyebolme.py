def f(x):
    return (x**2-4*x+3)

x1 = int(input("Başlangıç tahminini giriniz: "))
x2 = int(input("Bitiş tahminini giriniz: "))
delta = 0.001

if(f(x1)*f(x2) == 0):
    print("Tahminlerden biri denklem kökü.")
elif(f(x1)*f(x2) > 0):
    print("Bu aralıkta tek sayida kök yok.")
else:
    while(abs(x2-x1 > delta)):
        xr = (x1+x2)/2
        if(f(xr) == 0):
            print("denklemin kökü=",xr)
            break
        elif(f(x1)*f(xr) < 0):
            x2 = xr
        else:
            x1 = xr
    else:
        print(xr)
