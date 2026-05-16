class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca =  marca
        self.modelo = modelo
        self.ano  =  ano


    def __eq__(self, outro):
        return(
          
        self.marca == outro.marca and 
        self.modelo == outro.modelo and 
        self.ano == outro.ano


        ) 
        
        
c1  =  Carro('ford','fiesta','2024')
c2  =  Carro('Volks','fusca','2020')
c3  =  Carro('ford','fiesta','2024')



print(c1 == c3)


print(c2 == c1)