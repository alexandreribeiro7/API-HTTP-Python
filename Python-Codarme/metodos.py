class Evento:
    def metodo_instacia(self):
        return ("Método de instância chamado", self)
    
    @classmethod
    def metodo_classe(cls):
        return ("Método de classe chamado", cls)
    
    @staticmethod
    def metodo_estatico():
        return "Estático chamado"
    
ev = Evento()
a = ev.metodo_classe()
print(a)