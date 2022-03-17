import json 

class Query():
  def __init__(self):
    #pass
    with open("banco_dados.json", "r") as bd:
      self.dados = json.load(bd)
    #bd =  open("banco_dados.json", "r")
    #bd.close()

  def consulta(self):
    print("Digite o nº da consulta.")
    opcao = input("1.ID\n2.Dados do usuário\n")
    
    if opcao == "1":
      for id in self.dados:
        print(id)
    elif opcao == "2":
      id_consulta = input("Digite o id a ser consultado: ")
      for id, info_usuario in self.dados.items():
        if id == id_consulta:  
          nome = info_usuario['nome']
          idade = info_usuario['idade']
          nacionalidade = info_usuario['nacionalidade']

          print("\nDADOS CADASTRAIS DO USUÁRIO")
          print(f"ID: {id}\nNOME: {nome}\nIDADE: {idade}\nNACIONALIDADE: {nacionalidade}")




