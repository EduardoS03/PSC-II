class computadores:
    def __init__(self, so, cpu, ram, usuario):
        self.usuario= usuario
        self.so = so
        self.cpu = cpu
        self.ram = ram


    def ligar(self):
        print(f"O computador está ligando ... Perfil = {self.usuario}")

    def config(self):
        print(f'O Sistema é {self.so}, A CPU é {self.cpu} e a ram é {self.ram}')

    def desligar(self):
        print(f"O computador está desligando ... Perfil = {self.usuario}")

classe = computadores(
    cpu= 'i7-9900', 
    ram= '16gb',
    so= 'Linux',
    usuario= 'Usuario 1'

    )

classe1 = computadores(
    cpu= input("Digite a CPU : "), 
    ram= input("Digite a Ram : "),
    so= input("Digite o Sistema Operacional : "),
    usuario= input("Digite Nome do Usuario : ")
    )

classe.ligar()
classe1.ligar()
classe.config()
classe1.config()
classe.desligar()
classe1.desligar()