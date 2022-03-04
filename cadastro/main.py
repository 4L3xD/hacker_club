from userInfo import User
from base_course import BaseCourse
from data_science import DataScience
from infoSec import InfoSec

print("Olá! Vamos aprender computação.")
nome = input("Digite seu nome: ").capitalize()

print("\nÁreas em TI\n1. Ciência de Dados\n2. Segurança da Informação")
print(f"""\nDIGITE O NÚMERO da sua área de interesse, {nome}.
Caso, sua área de interesse não esteja nas opções escreva o nome dela:""")
area = input().lower()

if area == "1":
    cadastro = User().cadastro(nome, "Ciência de Dados")
    DataScience(nome).knowledge_test()
elif area == "2":
    cadastro = User().cadastro(nome, "Segurança da Informação")
    InfoSec(nome).knowledge_test()
else:
    cadastro = User().cadastro(nome, area)
    BaseCourse(nome).knowledge_test()
#TO DO: Criar exceções para usuários Q.A
