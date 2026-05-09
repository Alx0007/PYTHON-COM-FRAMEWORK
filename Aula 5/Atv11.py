
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo =  titulo
        self.autor = autor
        self.ano = ano
        self.dispo = True

    def emprestrar(self):
      nome  = input('nome: ')
    #   print(self.dispo)
      emprestar =  input('Emprestar? ')
      if emprestar == 'sim':
        if nome  == self.titulo:
            if self.dispo == True:
                print(self.dispo)
                print('esta disponivel ...')
                self.dispo = False
                print('Emprestado')
                return self.dispo

            else:
                print('Não esta diponivel')
        else:
            print('Não temos esse livro...')
    def devolver(self):
        self.dispo = True
        print('Livro devolvido')
        return self.dispo
    def info(self):
        return [
        self.titulo,
        self.autor,
        self.ano,
        self.dispo 
        ]


livro =  Livro('Cisne negro', 'taleb','2012')
livro.emprestrar()
livro.devolver()
print(livro.info())
