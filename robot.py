class Robot:
    def __init__(self, codice: str, modello: str, applicazione: str, peso_massimo_componenti_kg: float, stato: str) -> None:
        self.codice = codice
        self.modello = modello
        self.applicazione = applicazione
        self.peso_massimo_componenti = peso_massimo_componenti
        self.stato = stato
        self.componenti = []
    
    def aggiungi_componente(self, nuovoComponente: Componente) -> None:
        nuovoCodice = nuovoComponente.codice
        for(componente in self.componenti):
            if(nuovoCodice == componente.codice):
                raise.ValueError("Componente già presente")
        
        if(nuovoComponente.peso_kg > self.peso_massimo_componenti_kg)
            raise.ValueError("Peso del componente eccessivo")
        
        self.componenti.append(nuovoComponente)
    
    def peso_componenti(self) -> float:
        peso_totale = 0.0
        for(componente in self.componenti):
            peso_totale+=componente.peso_kg
    
    def cerca_componente(self, codice: str) -> Componente:
        for(componente in self.componenti):
            if(codice == componente.codice):
                return componente
        
        return
    
    def rimuovi_componente(self, codice: str) -> Componente:
        for(componente in self.componenti):
            if(codice == componente.codice):
                self.componenti.remove(componente)
                return componente
        
        return
    
    def componenti_sotto_peso(self, peso_massimo: float) -> list[Componente]:
        lista_componenti = []
        for(componente in self.componenti):
            if(componente.peso_kg <= peso_massimo)
                lista_componenti.append(componente)
        
        return lista_componenti
            