class monstruo():
    def __init__(self, ataque, vida, destreza):
        self.ataque = ataque
        self.vida = vida
        self.destreza = destreza
    
    def __str__(self):
        return "Vida: {}, Ataque: {}, Destreza: {}".format(self.vida, self.ataque, self.destreza)

class normal(monstruo):
    def __init__(self, ataque, vida, destreza, velocidad):
        super().__init__(ataque, vida, destreza)
        self.velocidad = velocidad

    def __str__(self):
        return "{} - Velocidad: {}".format(super().__str__(), self.velocidad)

class rapido(monstruo):
    def __init__(self, ataque, vida, destreza, velocidad):
        super().__init__(ataque, vida, destreza)
        self.velocidad = velocidad  # Se debe asignar correctamente
    
    def __str__(self):
        return "{} - Velocidad: {}".format(super().__str__(), self.velocidad)

class escudero(monstruo):
    def __init__(self, ataque, vida, destreza, velocidad, escudo):
        super().__init__(ataque, vida, destreza)
        self.velocidad = velocidad  # Se debe asignar correctamente
        self.escudo = escudo

    def __str__(self):
        return "{} - Velocidad: {}, Escudo: {}".format(super().__str__(), self.velocidad, self.escudo)

class boss1(monstruo):
    def __init__(self, ataque, vida, destreza, escudo, rango, evasion):
        super().__init__(ataque, vida, destreza)
        self.escudo = escudo
        self.rango = rango
        self.evasion = evasion

    def __str__(self):
        return "{} - Escudo: {}, Rango: {}, Evasión: {}".format(super().__str__(), self.escudo, self.rango, self.evasion)

# Ejemplo de uso:
m1 = normal(50, 100, 30, 20)
m2 = rapido(60, 80, 40, 50)
m3 = escudero(40, 120, 20, 10, 30)
m4 = boss1(100, 300, 50, 40, 60, 25)

print(m1)
print(m2)
print(m3)
print(m4)
