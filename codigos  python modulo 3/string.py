# -*- coding: utf-8 -*-
"""string.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J-G46XFU-OWHldSNcbxtgEKVaDu0ZgV5
"""

'verusca' + 'taiane'

x="rio"
y='janeiro'
print(x+y)

a1= 'consolação'
a2='sola'

print(a1 in a2)
print(a2 in a1)
print('sola' not in a2)

len("paralelepipedo")

len("")

a1= "miauscula"
a2="minuscula"
a3 = "escola"
print(a1.upper())
print(a1.lower())
print(a2.upper())
print(a2.lower())
print(a3.title())

c1="boa pedra"
print(c1.replace("pedra","merda"))

print(c1.startswith("boa"))
print(c1.endswith("bacana"))
print(c1.find('pedra'))

print(c1.split())
print(c1.split(","))

"""converter tipos de  dados"""

nascimento = 1988
ano_atual = 2023
idade = ano_atual - nascimento 
print('eu tenho',idade,'anos')

"""concatenar string com inteiro conversão de dados"""

nascimento = 1988
ano_atual = 2023
idade = ano_atual - nascimento 
saida=('eu tenho '+ str ( idade) +' anos')
print(saida)

saida2 =str(idade)
print(int(saida2)-3)

"""conversão do tipo inteiro

"""

print(float(10))
print(bool(-1))
print(bool(0))
print(str(999))

"""conversão do tipo float"""



print(int(9.9999))
print(bool(-0.99))
print(str(-0.99))

"""conversão do tipo bool"""

print(int(True))
print(float(True))
print(str(True))

"""conversão tipo string"""

print(int('-99'))
print(float('-0.99'))
print(bool('palavra'))
print(bool(""))

"""Formatação de dados utilizando F-string

"""

nascimento=1988
ano_atual=2023
idade= ano_atual - nascimento
print(f'eu tenho {idade} anos')



nascimento=1989
ano_atual=2023
print(f'eu tenho {ano_atual-nascimento} anos')