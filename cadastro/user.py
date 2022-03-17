from password import Password
import json
import random

class User():
  def __init__(self):
    pass
    
  def cadastro(self):

    self.id = random.randint(0000, 9999)
    try:
      bd = open('banco_dados.json', 'r') # 'r' = "read"
    except FileNotFoundError:
      bd = open("banco_dados.json", "w") # "w" = "write"
      bd.write("{}")
      bd.close()
      bd = open('banco_dados.json', 'r')
      
    dados = json.load(bd)
      
    while self.id in dados:
      self.id = random.randint(0000, 9999)
      #Testes da estrutura while
      #print(cod)
      #print("ID já existe!")
      #print("{}".format(self.id))
      #print(f"{self.id}")
    
    self.nome = input("Digite seu nome: ")
    self.idade = input("Digite tua idade: ")
    self.nacionalidade = input("Digite sua nacionalidade: ")
    self.senha = Password().cadastro()
  
    self.banco_dados = {}
    self.banco_dados[self.id] = {}
    self.banco_dados[self.id]['nome'] = self.nome.strip()
    self.banco_dados[self.id]['idade'] = self.idade.strip()
    self.banco_dados[self.id]['nacionalidade'] = self.nacionalidade.strip()
    self.banco_dados[self.id]['senha'] = self.senha
    
    with open('banco_dados.json', 'r+') as json_file:
      dados.update(self.banco_dados)
      json.dump(dados, json_file, indent=3, ensure_ascii=False)
    return print("Seu cadastro foi finalizado!")