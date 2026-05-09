class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f"Contato {contato.nome} adicionado com sucesso!")

    def listar_contatos(self):
        print("\n--- Lista de Contatos ---")
        for c in self.contatos:
            print(f"Nome: {c.nome} | Tel: {c.telefone} | Email: {c.email}")

    def buscar_contato(self, nome):
        print(f"\nBuscando por: {nome}...")
        encontrado = False
        for c in self.contatos:
            if c.nome.lower() == nome.lower():
                print(f"Encontrado! Telefone: {c.telefone}, Email: {c.email}")
                encontrado = True
        if not encontrado:
            print("Contato não encontrado na agenda.")

contato1 = Contato("Alice", "9999-1111", "alice@email.com")
contato2 = Contato("Bruno", "8888-2222", "bruno@email.com")

minha_agenda = Agenda()
minha_agenda.adicionar_contato(contato1)
minha_agenda.adicionar_contato(contato2)

minha_agenda.listar_contatos()

minha_agenda.buscar_contato("Alice")
minha_agenda.buscar_contato("Carlos")