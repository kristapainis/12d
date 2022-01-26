import math
mala=int(input("Ievadi kvadrāta malas garumu centimetros: "))
laukums1=mala*mala
laukums2=(mala+5)*(mala+5)
summa=laukums2/laukums1
atskiriba=summa*100
rezultats=math.ceil(atskiriba)
print(f'Kvadrāta laukums mainās par {rezultats}%')