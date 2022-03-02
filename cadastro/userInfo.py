from password import Password
import json
import random

class User():
  def __init__(self):
    pass
    
  def cadastro(self):
    self.id = random.randint(1000, 9999) # TO DO: pode duplicar valores, tratar!
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
    
    try:
      db = open('banco_dados.json', 'r')
    except:
      db =  open('banco_dados.json', 'w')
      db.write('''[
                    {
                    "ID":
                    {
                    "nome": "User Name",
                    "idade": "age",
                    "nacionalidade": "nationality",
                    "senha": "encrypted password"
                    }
                    }
                    ]''')
      db.close()
      db = open('banco_dados.json', 'r')
    
    json_db = json.load(db)
    json_db.append(self.banco_dados)

    db =  open('banco_dados.json', 'w')
    json.dump(json_db, db, indent=3, ensure_ascii=False)

    return print("Seu cadastro foi finalizado!")
