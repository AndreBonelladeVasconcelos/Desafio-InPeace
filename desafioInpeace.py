# Import Sys, Recebendo Argumentos Padronizados
import sys

try:
    arquivo_base = sys.argv[1]      # a.xml
    novo_arquivo = sys.argv[2]      # b.xml
    atributo_tag = sys.argv[3]      # colorPrimary
    valor_novo_tag = sys.argv[4]    # A2A2A2
except:
    print("""Padrao de uso: "Arquivo Base" "Novo Arquivo" "Atributo da Tag" "Novo Valor da Tag""")

#print(f'{arquivo_base}\n{novo_arquivo}\n{atributo_tag}\n{valor_novo_tag}')

# Importando o Arquivo .xml
import xml.etree.ElementTree as ET
tree = ET.parse(arquivo_base)
root = tree.getroot()

for colors in root.iter(): # Rodar pela Raiz
    #print({colors.text})
    #print(colors.tag)
     for attribute in colors.attrib:
        #print(f'{colors.attrib}')
        #print(f'{colors.attrib[attribute]}')   # Entra na tag e pega o atributo
        if atributo_tag == colors.attrib[attribute]:   # Atributo a ser mudado for igual linha da seguencia
            colors.text = valor_novo_tag

tree.write(novo_arquivo)   # Criar novo aquivo  .xml