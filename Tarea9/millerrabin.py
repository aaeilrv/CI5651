from random import randint

def miller_rabin(a, n):
    k = 0
    m = 0
    while True:
        if (n - 1) % 2**k == 0:
            m = (n - 1) // 2**k
            k += 1
        else:
            break
    k -= 1
    
    b = pow(a, m, n)
    
    if b == 1 or b == n - 1:
        return 'Es primo.'
    
    for _ in range(k):
        b_1 = pow(b, 2, n)
        if b_1 == n - 1:
            return 'Es primo.'
    return 'No es primo.'

def get_rand(n):
    return miller_rabin(randint(2, n - 1), n)

n = 161123316112331611233
print(get_rand(n))
