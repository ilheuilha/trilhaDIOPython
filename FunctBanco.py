import textwrap

def exibir_menu(): 

    menu = """"

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    return input(textwrap.dedent(menu))

def depositar(deposito, saldo, extrato, /):
    
    if deposito > 0:
        saldo += deposito

        extrato += f"Realizado o deposito de R$ {deposito:.2f}"

        print(extrato)
 
    else: 
        print("Erro ao depositar. Favor tentar novamente")

    return saldo, extrato            


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = exibir_menu()

        if opcao  == "d":
            
            deposito = int(input("Digite o valor do deposito "))
            
            saldo, extrato = depositar(deposito, saldo, extrato)

        elif opcao  == "s":
            
                if numero_saques < LIMITE_SAQUES:
                        
                    saque = float(input("Digite do valor do saque "))

                    if saldo == 0:
                        print("limite insuficiente")
                    else:    
                        if saque > limite:
                            print("Valor permitido de saque excedido")
                        if saque > saldo:
                            print("Saldo insuficiente")

                        else:

                            saldo -= saque

                            numero_saques += 1

                            print(f"Você sacou R$ {saque:.2f} e tem de saldo R$ {saldo:.2f} ")
                else:
                    print("Você estourou o limite de saque permitido")
    
        elif opcao == "e":

            print("============== EXTRATO ===============")
            print(f"O seu saldo atual é de R$ {saldo:.2f}")
            print("============== EXTRATO ===============")

        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
