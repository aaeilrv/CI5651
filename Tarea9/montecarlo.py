import random 

def freivald(a, b, c) :

    N = len(a)
     
    s = [0] * len(a)
     
    for i in range(0, N) :
        s[i] = (int)(random.randrange(509090009) % 2)
 
    br = [0] * N
     
    for i in range(0, N) :
        for j in range(0, N) :
            br[i] = br[i] + b[i][j] * s[j]
 
    cr = [0] * N
    for i in range(0, N) :
        for j in range(0, N) :
            cr[i] = cr[i] + c[i][j] * s[j]

    axbr = [0] * N
    for i in range(0, N) :
        for j in range(0, N) :
            axbr[i] = axbr[i] + a[i][j] * br[j]
 
    for i in range(0, N) :
        if (axbr[i] - cr[i] != 0) :
            return False
             
    return True

def esInversa(a, b, c, k) :     
    for _ in range(0, k) :
        if (not freivald(a, b, c)) :
            return False
    return True
 
a = [[1, 2, 1], [0, 1, 0], [2, 0, 3]]
b = [[3, -6, -1], [0, 1, 0], [-2, 4, 1]]
c = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
k = 2
N = 100
 
print(f'\n¿Es {b} la inversa de {a}?')
total_no = 0
total_si = 0
for i in range(0, N) : 
    if (esInversa(a, b, c, k)) :
        total_si += 1
    else :
        total_no += 1

print(f'Respondió SI {total_si} veces. (Opción correcta)')
print(f'Respondió NO {total_no} veces.')
print(f'Porcentaje de aciertos: {total_si / N * 100}%')