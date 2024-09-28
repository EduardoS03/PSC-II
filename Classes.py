class Computador:
    def  __init__(self, ram,processador, fonte, ms):
              self.ram = ram
              self.processador = processador
              self.fonte = fonte
              self.ms = ms
      
    def introducao(self):
              print(f"{self.ram} {self.processador} {self.fonte} {self.ms}")

comp = Computador('16 GB','Ryzen 9','650W','15TB')
comp.introducao()
 