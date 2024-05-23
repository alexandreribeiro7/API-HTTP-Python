class Evento:
    def __init__(self, nome):
        self.nome = nome


ev = Evento("Aula de python")
ev2 = Evento("Aula de Javascript")

print(ev.nome)
print(ev2.nome)