n = int(input('Informe um número: '))
t1 = 0
t2 = 1

cont = 0
print(f'{t1} -> {t2}', end='')

pertence = (n== t1 or n == t2)
while t2 <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')

    if t3 == n:
        pertence = True
    t1 = t2
    t2 = t3
    

if pertence:
    print(f'\n O número {n} pertence a sequência de Fibonacci')
else:
    print(f'\nO número {n} não pertence a sequencia de Fibonacci.')


#Já tinha até me esquecido o que era Fibonacci kkkkk