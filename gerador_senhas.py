
import string
import random
import os


letters = string.ascii_letters
numbers = string.digits
special = string.punctuation

menu = '''Gerador de Senhas Fortes
1 - Gerar Senhas Fortes
2 - Exportar txt
0 - Sair
'''

def generate_passkey():
    """
    Retorna uma senha segura de 8, 10 ou 12 caracteres

    Returns:
        string: Senha gerada a partir do processamento randomizado de dados
    """
    lengths = [8,10,12]
    length = 0
    passkey = ''
    deck = [letters, numbers, special]
    
    while (length not in lengths):
        try:
            length = int(input("Quantos caracteres deve conter a senha, 8, 10 ou 12?\n")) 
        except ValueError:
            print("Entrada inválida! Digite um numero.\n")
    
    while len(passkey) < length:
        random.shuffle(deck)
        x = random.randrange(0,3)
        y = random.randrange(0,len(deck[x]))
        passkey += deck[x][y]
    print("-------------------------")
    print('Gerando a senha...')
    print("-------------------------")
    
    return passkey + '\n'

def txt_export(passkey):
    """Exportação de senha em arquivo texto

    Args:
        passkey string: senha gerada pelo método generate_passkey

    Returns:
        string: caminho absoluto do arquivo gerado
    """
    file = "senha_exportada.txt"
        
    with open(file, 'w', encoding="utf-8") as arquivo:
        arquivo.write(passkey)
    
    return os.path.abspath(file)
    
    
    


def main():
    """Método main
    Ele controla o fluxo de execução do programa
    """
    option = 9
    passkey = ''
    
    while option != 0:
        
        print(menu)
        try:
            option = int(input("Digite a opção desejada:\n"))
        except ValueError:
            print("Entrada inválida! Digite um numero.\n")
            continue
        
        if option == 1:
            passkey = generate_passkey()
            print(passkey)
            
        elif option == 2:
            absolute_path = txt_export(passkey)
            print(f"Senha salva no arquivo!{absolute_path}")
            
        elif option == 0:
            print("Saindo.....")
            break
        else:
            print("Opcao Inválida")
    
    

if __name__ == "__main__":
    main()