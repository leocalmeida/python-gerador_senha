import string

letters = string.ascii_letters
numbers = string.digits
special = string.punctuation

menu = '''Gerador de Senhas Fortes
1 - Gerar Senhas Fortes
2 - Exportar txt
0 - Sair
'''

def generate_passkey():
    length = int(input("Quantos caracteres deve conter a senha, 8, 10 ou 12?\n")) 
        
    pass


def main():
    
    option = 9
    while option != 0:
        print(menu)
        option = int(input("Digite a opção desejada:\n"))
        if option == 1:
            # generate_passkey()
            pass
        elif option == 2:
            pass
        else:
            print("invalid option")
    
    

if __name__ == "__main__":
    main()