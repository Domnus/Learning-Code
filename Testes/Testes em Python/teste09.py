from colorama import Fore
from colorama import Back
from colorama import Style

def cadastrar():
    nome, telefone = input("Digite o nome e telefone separados por um espaço: ").split()
    if nome in agenda:
        print(f"\n{Back.RED}Contato já cadastrado!{Style.RESET_ALL}\n")
    else:
        agenda[nome] = int(telefone)
        print(f"\n{Fore.GREEN}Contato cadastrado com sucesso!{Style.RESET_ALL}\n")

def consultar():
    nome = input("Digite o nome para consulta: ")
    if nome in agenda:
        print(f"{Fore.GREEN}Contato: {nome} | Telefone: {agenda[nome]}{Style.RESET_ALL}")
    else:
        print(f"\n{Back.RED}Contato não cadastrado!{Style.RESET_ALL}\n")

def apagar():
    nome = input("Informe o contato que deseja apagar: ")
    
    if nome in agenda:
        agenda.pop(nome) 
        print(f"\n{Fore.GREEN}Contato apagado com sucesso!{Style.RESET_ALL}\n")
    else:
        print(f"\nContato inválido!{Style.RESET_ALL}\n")

def alterar():
    nome = input("Informe o contato que deseja alterar: ")
    if nome in agenda:
        telefone = int(input("Digite o novo número: "))
        agenda[nome] = telefone
        print(f"\n{Fore.GREEN}Contato alterado com sucesso!{Style.RESET_ALL}\n")
    else:
        print(f"\n{Back.RED}Contato não cadastrado!{Style.RESET_ALL}\n")

def listar():
    for i in agenda:
        print(f"{Fore.GREEN}Contato: {i} | Telefone: {agenda[i]}{Style.RESET_ALL}")

def menu():
    print(f"{Fore.WHITE}-----Agenda Telefônica-----\n"
          f"-> 1. Cadastrar\n"
          f"-> 2. Consultar\n"
          f"-> 3. Apagar\n"
          f"-> 4. Alterar\n"
          f"-> 5. Listar\n"
          f"-> 6. Sair{Style.RESET_ALL}")

    return input("Escolha a opção-> ")

def entradaInvalida():
    print(f"{Fore.RED}_______________________{Style.RESET_ALL}")
    print(f"{Fore.RED}|  Entrada Inválida!  |{Style.RESET_ALL}")
    print(f"{Fore.RED}-----------------------{Style.RESET_ALL}")

agenda = {}
while True:
    
    op = int(menu())
    if op == 1:
        cadastrar()
    elif op == 2:
        consultar()
    elif op == 3:
        apagar()
    elif op == 4:
        alterar()
    elif op == 5:
        listar()
    elif op == 6:
        break
    else:
        entradaInvalida()
