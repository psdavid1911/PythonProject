def funcao():
    try:
        funcao_errada()
    except ZeroDivisionError:
        print('deu divisao por zero')

def funcao_errada():
    try:
        print('vou tentar dividir')
        print(1 / 0)
    except:
        raise ZeroDivisionError

funcao()
