from numpy import prod
#dizi yapısıyla

x = [1, 2, 3, 4, 6, 7, 9]
y = [3, 5, 7, 9, 13, 15, 19]

a1 = ((len(x)*sum([x[i]*y[i] for i in range(len(x))])-sum(x)*sum(y))
      /(len(x)*sum([i**2 for i in x])-sum(x)**2))

a0 = (sum(y) - a1*sum(x))/len(x)

print(a1, a0)

#sozluk yapısıyla
x1 = {1:3, 2:5, 3:7, 4:9, 6:13, 7:15, 9:19}

a3 = ((len(x1)*sum([prod(i) for i in x1.items()]) - sum(x1)*sum(x1.values()))
      /(len(x1)*sum([i**2 for i in x1]) - sum(x1)**2))

a4 = (sum(x1.values()) - a3*sum(x1)) / len(x1)

print(a3,a4)



print(a0 + a1*5)

