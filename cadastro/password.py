from approved_pass import Approved
from caesar_cipher import Caesar

class Password():
  def __init__(self):
    pass
  
  def cadastro(self):
    self.senha = Approved().test_password()
    
    while self.senha == None:
      self.senha = Approved().test_password()
      
      # Reverse Cipher
      # http://inventwithpython.com/hacking (BSD Licensed)

    #translated = ''
  
    #i = len(self.senha) - 1

    #while i >= 0:
    #    translated = translated + self.senha[i]
    #    i = i - 1 #decrementação/subtração

    self.senha = Caesar(self.senha).cripto()
  
    return self.senha