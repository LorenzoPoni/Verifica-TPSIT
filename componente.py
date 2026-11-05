class Componente:
    def __init__(self, codice: str, nome: str, peso_kg: float) -> None:
        self.codice = codice
        self.nome = nome
        self.peso_kg = peso_kg
    
    def __str__(self) -> str:
        return f"Codice: {self.codice}, Nome: {self.nome}, Peso in kg: {self.peso_kg}"