class Boligrafo:
    def __init__(self,groso_punta:str,color:str) -> None:
        groso_punta = float(groso_punta)
        if groso_punta >= 1.4:
            groso_punta = True
        else:
            groso_punta = False
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = groso_punta
        self.color  = color
        self.cantidad_tinta = 80
    
    def escribir(self,texto:str)->str:
        valor_retorno = "No alcanza la tinta"

        if self.grosor_punta:
            if self.cantidad_tinta >= (len(texto)*2):
                self.cantidad_tinta -= (len(texto)*2)
                valor_retorno = texto
        else:
            if self.cantidad_tinta >= len(texto):
                valor_retorno = texto
                self.cantidad_tinta -= (len(texto))

        return valor_retorno

    def recargar(self,cantidad:int)->str:
        acumulador = self.cantidad_tinta + cantidad
        if acumulador <= self.capacidad_tinta_maxima:
            self.cantidad_tinta = cantidad
            valor_retorno = "Lapicera recargada"
        else:
            self.cantidad_tinta = self.capacidad_tinta_maxima
            
            resto = self.capacidad_tinta_maxima - acumulador
            valor_retorno = f"Se recargó la lapicera y sobró {resto} cantidad de tinta"
        return valor_retorno
