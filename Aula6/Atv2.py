class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo =  titulo
        self.autor = autor
        self.ano = ano
        self.emprestado = False
        
    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return self.emprestado
            
            
    def devolver(self):
        self.emprestado = False         
        return self.emprestado
    
    def __str__(self):
        return f'{self.titulo} {self.autor} {self.ano}'

titulo, autor, ano = input('Livro: '), input('autor: '), input('ano ')

l1 =  Livro(titulo, autor, ano)

print('Emprestado? - ', l1.emprestar())

print('Emprestado? - ',l1.devolver())

print(l1)