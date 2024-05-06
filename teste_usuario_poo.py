# TODO: Crie uma classe UsuarioTelefone.
# TODO: Defina um método especial `__init__`, que é o construtor da classe.
# O método `__init__`, irá inicializar os atributos da classe: `nome`, `numero` e `plano`.
# TODO: Aplique o conceito de encapsulamento, onde os atributos serão encapsulados dentro da classe.


class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

    def usuario_novo():

        nome = input("Digite o seu nome: ")
        numero = int(input("Digite o seu numero"))
        plano = input("Digite o seu plano")

        usuario = UsuarioTelefone(nome, numero, plano)

        # TODO: Crie um novo objeto `UsuarioTelefone` com os dados fornecidos:

        return usuario


novo_usuario = UsuarioTelefone.usuario_novo()

print(novo_usuario)
