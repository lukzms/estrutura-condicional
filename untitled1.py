# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TKgTj-IAJ-bTVHwgW1x6uU1Ic3NNiHmV
"""

resposta= input('Deseja ir pra proxima tela')
if resposta == 'sim':
   print ('você foi pra outra tela')
else:
    print('você saiu do sistema')

nome = input ('Informe o nome de usuário:')
sexo = input ("Informe 'f' para feminino e 'm' para masculino:").upper()
if(sexo == 'M'):
    sexo = 'o'
elif(sexo == 'F'):
    sexo = 'a'
usuario = int(input(' informe o tipo de usuario \n 1 - para adiministrador \n 2 para usuario comum \3 - para membros associado'))

if(usuario == 1):
    usuario = 'administrador do sistema'
elif(usuario == 3):
    usuario = 'membro associado'
elif(usuario == 2):
    usuario = 'usuario comum'
else:
    usuario = 'usuario não cadastrado'
print(f'seja bem vind{sexo} {nome}, a sua licença e de {usuario}')