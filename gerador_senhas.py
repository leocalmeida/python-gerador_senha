import string
import random

letters = string.ascii_letters
numbers = string.digits
special = string.punctuation

menu = '''Gerador de Senhas Fortes
1 - Gerar Senhas Fortes
2 - Exportar txt
0 - Sair
'''

def generate_passkey():
    lengths = [8,10,12]
    length = 0
    passkey = ''
    deck = [letters, numbers, special]
    
    while (length not in lengths):
        length = int(input("Quantos caracteres deve conter a senha, 8, 10 ou 12?\n")) 
    
    while len(passkey) < length:
        random.shuffle(deck)
        x = random.randrange(0,3)
        y = random.randrange(0,len(deck[x]))
        passkey += deck[x][y]
    print("-------------------------")
    print('Gerando a senhas...')
    print("-------------------------")
    
    return passkey + '\n'

def txt_export(passkey):
    pass


def main():
    
    option = 9
    while option != 0:
        passkey = ''
        
        print(menu)
        option = int(input("Digite a opção desejada:\n"))
        
        if option == 1:
            passkey = generate_passkey()
            print(passkey)
            
        elif option == 2:
            txt_export(passkey)
            
        elif option == 0:
            print("Saindo.....")
            break
        else:
            print("invalid option")
    
    

if __name__ == "__main__":
    main()