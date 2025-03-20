class monstruo():
    def __init__(self,ataque,vida,destreza):
        self.ataque=ataque
        self.vida=vida
        self.destreza=destreza
    def __str__(self):
        return "{},tu vida es {},tu ataque es{},tu destreza es{}".format(self.ataque,self.vida,self.destreza)
class normal(monstruo):
    def __init__(self,ataque,vida,destreza,velocidad):
        super().__init__(ataque,vida,destreza)
        self.velocidad=velocidad
    def __str__(self):
        return "{}- tu velocidad es {}".format(super().__str__(),self.velocidad)

class rapido(monstruo):
    def __init__(self,ataque,vida,destreza,velocidad):
        super().__init__(ataque,vida,destreza,velocidad)
    def __str__(self):
        return super().__str__()
