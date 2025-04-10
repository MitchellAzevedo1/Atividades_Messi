numero = int(input('Digite o número da tabuada:'))

for m in range(1, 11):
    print(f'f{numero} x {m} = {numero * m} ')

ciclos = 1
while ciclos <= 10:
    resultado = numero * ciclos

    print(f'{numero} x {ciclos} = {resultado}')
    #incremento
    ciclos += 1