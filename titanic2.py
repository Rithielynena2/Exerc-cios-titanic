import json
import csv
import funçoes
'''
#arquivo_json = open('data.json", "r")
#pessoas_json = json.load(arquivo_json)
# colocou a lista de outro arquivo nessa variavel

arquivo = open("data.csv","r")
pessoas = csv.DictReader(arquivo)
maior_idade = 0
menor_idade = 0
for p in pessoas:
    if int(p.get("idade")) >= 18:
        maior_idade += 1
    else:
        menor_idade += 1
print(maior_idade)
print(menor_idade)

'''
# COM BASE NO ARQUIVO TITANIC.CSV, QUANTAS PESSOAS SOBRERIVERAM E QUANTAS MORRERAM?

arquivo = open("titanic.csv","r")
titanic = csv.DictReader(arquivo)
morreram = 0
sobreviveram = 0
for t in titanic:
    if int(t.get("Survived")) == 0:
        morreram += 1
    else:
        sobreviveram += 1
print(f'Sobreviveram {sobreviveram} pessoas')
print(f'Morreram {morreram} pessoas')

# ou

arquivo = open("titanic.csv","r")
titanic = csv.DictReader(arquivo)
dados = funçoes.verificar_sobreviventes(titanic)
print (dados)


#Calcule a média da idade dos passageiros

arquivo = open("titanic.csv","r")
titanic = list(csv.DictReader(arquivo))
media_idades = funçoes.media_dos_passageiros(titanic)
print (media_idades)

# Qual o nome do passageiro mais jovem?

menor_idade= funçoes.menor_idade(titanic)
print(menor_idade)

#Conte e exiba o numero total de passageiros por sexo

contagem_por_sexo = funçoes.contar_passageiros_por_sexo(titanic)
print(contagem_por_sexo)



