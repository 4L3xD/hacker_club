from password import Password
import json
import random

class User():
  def __init__(self):
    pass
    
  def cadastro(self, nome, area):
    self.id = random.randint(1000, 9999) # TO DO: pode duplicar valores, tratar!
    self.idade = input("Digite tua idade: ")
    self.nacionalidade = input("Digite sua nacionalidade: ")
    self.senha = Password().cadastro()

    self.banco_dados = {}
    self.banco_dados[self.id] = {}
    self.banco_dados[self.id]['nome'] = nome.strip()
    self.banco_dados[self.id]['idade'] = self.idade.strip()
    self.banco_dados[self.id]['nacionalidade'] = self.nacionalidade.strip()
    self.banco_dados[self.id]["area"] = area
    self.banco_dados[self.id]['senha'] = self.senha
    
    try:
      db = open('banco_dados.json', 'r')
    except:
        db = open('banco_dados.json', "w")
        db.write("{}")
        db.close()

    with open('banco_dados.json', "r+", encoding="utf8") as json_file:
      data = json.load(json_file)
      data.update(self.banco_dados)
      json_file.seek(0)
      json.dump(data, json_file, indent=2, ensure_ascii=False)

    return print(f"{nome}, seu cadastro foi concluído!")

# Referências:
# https://www.kite.com/python/answers/how-to-append-to-a-json-file-in-python