class Funcionario:                                 
    def __init__(self, id, nome, cargo, ativo):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.ativo = ativo
    def situacao(self):          
        return "Ativo" if self.ativo else "Inativo"
