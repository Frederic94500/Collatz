print ("Entrer une valeur:")
n = int(input())
print (n)
tdvol = 1
while n!=1:
    tdvol = tdvol + 1
    if n%2==0:
        n = n/2
        print (n)
    else:
        n = 3*n+1
        print (n)
print ("Le temps de vol est égale à" , tdvol)