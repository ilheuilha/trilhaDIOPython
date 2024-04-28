import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

def exibir_menu(): 

    menu = """"

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova conta
    [nu] Novo usuário
    [lc] Listar contas
    [q] Sair

    => """

    return input(textwrap.dedent(menu))

class Historico:
    def __init__(self):
        self._transacao = []
    
    def transacoes(self):
        return self._transacao
    

    def adicionarTransacao(self):
        self._transacao.append(
            { "tipo": Transacao.__class__.__name__,
             "valor": Transacao.valor, 
             "data": datetime.now().strftime("%d-%m-%Y"), }
        )

class Conta:
    def __init__(self, numero, cliente):

        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._histórico = Historico()

    def saldo(self):
       return self._saldo
    
    @classmethod
    def nova_conta (cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def sacar(self, saque):
        saldo = self.saldo
        excedeu_valor = saque > saldo

        if excedeu_valor:
            print("O saque é maior que o saque ")

        elif saldo > 0:
        
            self._saldo -= saque
            
            print(f"\nVocê sacou R$ {saque:.2f} e tem de saldo R$ {saldo:.2f} \n")

            return True
        else:
            print("Ocorreu um erro. Tente novamente mais tarde")
        
        return False
    
    def __str__(self) -> str:
        return f"""\
            Agencia: \t{self.agencia}
            C/C: \t\t{self._numero}
            Titular: \t{self._cliente.nome}
            """

    @property
    def depositar(self, deposito):
        
        if deposito > 0:
        
            self._saldo += deposito

            print(f"Realizado o deposito de R$ {deposito:.2f} \n\n")

        else: 

            print("Erro ao depositar. Favor tentar novamente")
            return False

        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        self._limite = limite
        self._limite_saques = limite_saques
        super().__init__(numero, cliente)
    
    def sacar(self,valor):
        numero_saques = len([Transacao for transacao in self.historico.transacoes if transacao["tipo"] ==  Saque.__name__]
                            )
        
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("Limite excedido")
        elif excedeu_saques:
            print("Limite de saque excedido")
        else:
            return super().sacar(valor)
        
        return False
    def __str__(self) -> str:
       return f"""\
            Agencia: \t{self.agencia}
            C/C: \t\t{self._numero}
            Titular: \t{self._cliente.nome}
            """

class Cliente():
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = []
    
    def realizarTransacao(self, conta, transacao):
        self.conta = conta
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Transacao(ABC):
    @abstractclassmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor) -> None:
        self.valor = valor

    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
    
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
class Deposito(Transacao):
    def __init__(self, valor) -> None:
        self.valor = valor
    
    @property
    def valor(self):
        return self.valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
