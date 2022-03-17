from approved_pass import Approved

class Password():
  def __init__(self):
    pass
  
  def cadastro(self):
    self.senha = Approved().test_password()
    
    while self.senha == None:
      self.senha = Approved().test_password()
      
      # Reverse Cipher
      # http://inventwithpython.com/hacking (BSD Licensed)
    #senha = "abcd"
    #translated = 'dcba'
    translated = ''
    
    # "abcd" ==> índices: a = 0, b = 1, c = 2, d = 3
    # len("abcd") = 4 caracteres
    i = len(self.senha) - 1
  
    while i >= 0:
        translated = translated + self.senha[i]
        i = i - 1 #decrementação/subtração
  
    return translated