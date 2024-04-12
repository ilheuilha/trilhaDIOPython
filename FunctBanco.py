import textwrap

def exibir_menu(): 

    menu = """"

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [lu] Listar usuário

    [q] Sair

    => """

    return input(textwrap.dedent(menu))

def depositar(deposito, saldo, extrato, /):
    
    if deposito > 0:
        saldo += deposito

        extrato += f"Realizado o deposito de R$ {deposito:.2f} \n\n"

        print("Deposito concluido com sucesso")
 
    else: 
        print("Erro ao depositar. Favor tentar novamente")

    return saldo, extrato       

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    
    excedeu_valor_saldo = saque > saldo
    excedeu_valor_limite = saque > limite
    excedeu_valor_limite_saque = numero_saques >= limite_saques

    if excedeu_valor_saldo:
        print(f"Valor indisponivel. Você tem R$ {saldo} de saldo")
    elif excedeu_valor_limite:
        print("Valor do limite excedido")
    elif excedeu_valor_limite_saque:
        print("A quantidade de saque por dia foi atingido")
    
    elif saldo > 0:
      
        saldo -= saque
        
        extrato += f"\nVocê sacou R$ {saque:.2f} e tem de saldo R$ {saldo:.2f} \n"

        numero_saques += 1    

        print("Saque concluido")

        
    else:
        print("Ocorreu um erro. Tente novamente mais tarde")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n ============== EXTRATO =============== ")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"O seu saldo atual é de \n R$ {saldo:.2f}")
    print("============== EXTRATO ===============")

def criarUsuario(usuarios):

    cpf = int(input("Digite o numero do cpf (Somente numeros) "))

    #if usuario != cpf:

    nome = input("Digite o nome do usuario: ")
    endereco = input("Digite a data de nascimento no formato (logradouro, nro - bairro - cidade/sigla estado):")
    dataNasc = input("Digite a data de nascimento (dd-mm-aaaa): ")

    usuarios.append({"nome": nome, "data_nascimento": dataNasc, "cpf": cpf, "endereco": endereco})

    print("Usuario cadastrado com sucesso")
        
def listaCPF():
    print("CPFs Cadastrados")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []

    while True:

        opcao = exibir_menu()

        if opcao  == "d":
            
            deposito = int(input("Digite o valor do deposito "))
            
            saldo, extrato = depositar(deposito, saldo, extrato)

        elif opcao  == "s":            
            
            saque = float(input("Digite do valor do saque "))

            saldo, extrato = sacar(saldo = saldo, saque = saque, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)


        elif opcao == "e":

            exibir_extrato(saldo, extrato=extrato)

        elif opcao =="nu":

           criarUsuario(usuarios)


        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
