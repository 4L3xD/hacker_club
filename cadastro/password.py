import re
import getpass #modulo que esconde a senha

class Approved():
    def __init__(self):
      pass
  
    def test_password(self):
        print("A senha deve ter mais de 8 digitos, e alem disso conter, no minimo, um caractere especial, uma letra minuscula, uma letra maiuscula e um numero.")
        password = getpass.getpass('Digite tua senha: ')
  
        minimal_number = 1
        minimal_upper_char = 1
        minimal_lower_char = 1
        minimal_special_char = 1
        minimal_len_char = 8

        tam, up, low, num, esp = False, False, False, False, False
      
        if len(password or ()) < minimal_len_char:
            print('Senha tem que ter no mínimo '+str(minimal_len_char)+' caracteres')
        else:
          tam = True
      
        if len(re.findall(r"[A-Z]", password)) < minimal_upper_char:
            print('Senha tem que ter no mínimo '+str(minimal_upper_char)+' letras maiusculas')
        else:
          up = True 
        
        if len(re.findall(r"[a-z]", password)) < minimal_lower_char:
            print('Senha tem que ter no mínimo '+str(minimal_lower_char)+' letras minusculas')
        else:
          low = True
          
        if len(re.findall(r"[0-9]", password)) < minimal_number:
            print('Senha tem que ter no mínimo '+str(minimal_number)+' numeros')
        else:
          num = True
          
        if len(re.findall(r"[~`!@#$%^&*()_+=-{};:'><]", password)) < minimal_special_char:
            print('Senha tem que ter no mínimo '+str(minimal_special_char)+' caracteres especiais')
        else:
          esp = True

        if esp == True and num == True and low == True and up == True and tam == True:
          print("Ta-dã! senha valida!")
          return password
          
