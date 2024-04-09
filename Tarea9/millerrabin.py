from random import randint

def BTest(a, n):
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
    print(f'\nb_0: {b}')
    
    if b == 1 or b == n - 1:
        return True
    
    for _ in range(k):
        b = pow(b, 2, n)
        print(f'b_{_ + 1}: {b}')
        if b == n - 1:
            return True
    return False

def millRap(n):
    a = randint(2, n - 1)
    print(f'\na: {a}')
    return BTest(a, n)

def millRabRep(n, k):
    for _ in range(k):
        print(f'\nIteración: {_}')
        if not millRap(n):
            return '\nNo es primo.'
    return '\nEs primo.'

n = 161123316112331611233
print(millRabRep(n, 10))