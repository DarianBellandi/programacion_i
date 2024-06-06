class PersonajeJuego:
    
    #ATRIBUTOS
    #nombre - poder_pelea - habilidad - puede_volar - usa_nanotecnologia

    #METODOS
    #constructor
    def __init__(self,nombre:str,poder_pelea:int,habilidad:str,vuela:bool,nano:bool) -> None:
        self.nombre = nombre
        self.poder_pelea = poder_pelea
        self.habilidad = habilidad
        self.puede_volar = vuela
        self.usa_nanotectonolia = nano

    def describirse(self):
        descripcion = f"{self.nombre} - {self.poder_pelea} - {self.habilidad}"
        if self.puede_volar:
            descripcion += "- Puede volar"
        else:
            descripcion += "- No puede volar"
        if self.usa_nanotectonolia:
            descripcion += "- Usa nanotecnología"
        else:
            descripcion += "- No usa nano"
        descripcion += "*" * 30
        return descripcion

    def volar(self,altura:int,velocidad:int):
        if self.puede_volar:
            print(f"{self.nombre}: estoy volando a {altura} y una velocidad de {velocidad}")
        else:
            print(f"{self.nombre} aún no puede")


    def atacar(self,enemigo):
        if self.poder_pelea > enemigo.poder_pelea:
            print(f"GANO: {self.nombre}")
            self.poder_pelea -= enemigo.poder_pelea
            enemigo.poder_pelea = 0
        else:
            if self.poder_pelea < enemigo.poder_pelea:
                print(f"GANO: {enemigo.nombre}")
                enemigo.poder_pelea -= self.poder_pelea
                self.poder_pelea = 0
            else:
                print(f"{self.nombre} y {enemigo.poder_pelea} EMPATARON")
                self.poder_pelea *= 0.9
                enemigo.poder_pelea *= 0.9