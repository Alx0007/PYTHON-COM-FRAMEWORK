class Contato():
     def __init__(self, nome, telefone, email):
          self.nome = nome
          self.telefone =  telefone
          self.email   =  email


class Agenda():
     def __init__(self):
        self.__contatos =  []

     def add_contato(self, contato):
          self.__contatos.append(contato)


     def lista_contato(self):
          for c in self.__contatos:
               print(c.nome, c.telefone, c.email)
     
     def buscar_contato(self, nome):
         for c in self.__contatos:
              if c.nome == nome:
                   print(c.nome, c.telefone,c.email)


agenda  = Agenda()

contato1 = Contato('ana','54464646', 'ana@gmail.com')

contato2 = Contato('ana2','54464646', 'ana@gmail.com')

agenda.add_contato(contato1)
agenda.add_contato(contato2)
agenda.lista_contato()
agenda.buscar_contato('ana')
        
            

