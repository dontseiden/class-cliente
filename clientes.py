clientes = []
class Cliente:
    def __init__(self, id: int, nome: str, idade: int, email: str):
        self.__id = id
        self.__nome = nome
        self.__idade = idade
        self.__h_ingresso = []
        self.__email = email
        
    def validar_idade(self):
        return self.__idade >= 18

    def ad_ingresso(self, ingresso):
        self.__h_ingresso.append(ingresso)

    def __ver_historico(self):
        return self.__h_ingresso

while True:
    n = int(input("""CLIENTE
    1 - CADASTRAR CLIENTE
    2 - VALIDAR IDADE
    3 - ADICIONAR INGRESSO
    4 - VER HISTORICO DE INGRESSOS
    5 - SAIR\n
    """))
    if n == 1:
        nome = input("Nome:\n")
        idade = int(input("Idade:\n"))
        email = input("E-mail:\n") 
        id = len(clientes)
        cliente = Cliente(id, nome, idade, email)
        clientes.append(cliente)
    elif n == 2:
        if len(clientes) == 0:
            print("Não há clientes para validar idade.")
        else:
            indice = int(input("Digite o id do cliente:\n"))
            
            if 0 <= indice < len(clientes):
                if clientes[indice].validar_idade():
                    print("O cliente é MAIOR de idade.")
                else:
                    print("O cliente é MENOR de idade.")
            else:
                print("ID de cliente inválido.")
            
    elif n == 3:
        local = input("Nome:\n")
        tipo = int(input("Idade:\n"))
        id = len(ingressos)
        ingresso = Ingresso(local, tipo)
        Ingresso.append(ingresso)

    elif n == 4:
        for i in range(len(ingressos)):
            print(f"Ingresso {i+1}")
            print(f"Local: {local_assento}")
            print(f"Tipo de ingresso: {tipo_ingresso}")
    elif n == 5:
        break
    else:
        print("O número informado não corresponde a nenhuma das opçoes disponíveis. Tente novamente.")