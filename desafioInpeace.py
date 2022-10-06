# Importando o Arquivo Base XML

import sys

try:
    arquivo_base = sys.argv[1]
    novo_arquivo = sys.argv[2]
    atributo_tag = sys.argv[3]
    valor_novo_tag = sys.argv[4]
except:
    print('Mais argumento que o padronizado')

import xml.etree.ElementTree as ET
mytree = ET.parse(arquivo_base)
myroot = mytree.getroot()

# Criar Lista
array_tag = []
array_tag_novo = []
# Nome Tag
nome_tag = str(input("Nome TAG: "))
# Receber Numeros de Mudanças de TAGs.
n = int(input(f'Quantos Atributos para substituir de <{nome_tag}>: '))

# For para receber os atributos.
for i in range(0, n):
    variavel, novo = input('Valor [Velho, Novo]').split()  # Receber valor
    array_tag.append(str(variavel))  # Adicionando a lista
    array_tag_novo.append(str(novo))
    #posicao = i.__index__()  # contar posicao na lista
    for colors in myroot.iter(nome_tag):
        colors.text = str(colors.text.replace(variavel, novo))

mytree.write(f'{novo_arquivo}.xml')

print(f'Novo Arquivo \"{novo_arquivo}\" Criado com Sucesso')


"""
Utilizar o script desafioInpeace.py para copiar o conteúdo de “a.xml” para “b.xml” alterando
a variável colorPrimary para A2A2A2.
python desafioInpeace "a.xml" "b.xml" colorPrimary A2A2A2

#2EC1D7
"""