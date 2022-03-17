from query import Query
from user import User

print("1.cadastro 2.consulta")
opcao = input()

if opcao == "1":
  User().cadastro()
elif opcao == "2":
  Query().consulta()






