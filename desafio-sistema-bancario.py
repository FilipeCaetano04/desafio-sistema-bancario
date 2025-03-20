menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3

while True:

    opc = input(menu)

    if opc == 'd':
        valor = float(input('Valor a ser depositado: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito de R$ {valor:.2f}\n'

        else:
            print('Depósito não realizado! Valor de depósito negativo!')
    
    elif opc == 's':

        # Verifica se ainda é possível fazer saques
        # Se não for, volta para o menu
        if numero_saques >= LIMITE_SAQUE:
            print('Saque não realizado! Número máximo de saques excedido!')
            continue
        
        # Pede o valor a ser sacado após a verificação
        saque = float(input('Valor a ser sacado: '))

        if saque > saldo:
            print('Saque não realizado! Saldo insuficiente!') 

        elif saque > limite:
            print('Saque não realizado! Valor excedeu o limite!')

        elif saque <= 0:
            print('Saque não realizado! Valor de saque incongruente!')
        else:
            # Lógica do saque após verificar as condições necessárias para efetua-lo
            saldo -= saque
            extrato += f'Saque de R$ {saque:.2f}\n'
            numero_saques += 1
        
    elif opc == 'e':
        print(' EXTRATO '.center(40, '='))
        print('Não foram realizado movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('=' * 40)

    elif opc == 'q':
        break

    else:
        print('Operação inválida, por favor selecione a operação desejada.')