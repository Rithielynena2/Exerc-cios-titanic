import json
import csv
import funcoes_2


#arquivo_json = open("data.json", "r")
#pessoas_json = json.load(arquivo_json)

arquivo = open("data.csv", "r")
pessoas = csv.DictReader(arquivo)

"""maior_idade = 0
menor_idade = 0
for p in pessoas:
    if int(p["idade"]) >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(maior_idade)
print(menor_idade)"""

arquivo = open("titanic.csv", "r")
titanic = list(csv.DictReader(arquivo))

"Com base no arquivo titanic.csv, quantas pessoas sobreviveram e quantas morreram?"
survived = funcoes.verificar_survived(titanic)
print(survived)

"Calcule e exiba a média de idades dos passageiros."
media_idade = funcoes.calcular_media_idade(titanic)
print(media_idade)

"Identifique e exiba o nome do passageiro mais jovem a bordo."

passageiro_mais_jovem = funcoes.pegar_passageiro_mais_jovem(titanic)
print(passageiro_mais_jovem)

"Conte e exiba o número total de passageiros por sexo."
contagem_por_sexo = funcoes.contar_passageiros_por_sexo(titanic)
print(contagem_por_sexo)

"Identifique e exiba o passageiro com a tarifa mais alta."
passageiro_tarifa_mais_alta = funcoes.pegar_passageiro_valor_mais_alto(titanic)
print(passageiro_tarifa_mais_alta)



"Calcule e exiba a idade média dos sobreviventes e dos não sobreviventes."

arquivo = open("titanic.csv", "r")
titanic = list(csv.DictReader(arquivo))
media_idades = funcoes_2.calcular_media_idade_sobreviventes(titanic)
print(media_idades)


"Calcule e exiba a porcentagem de sobreviventes em relação ao total de passageiros."
resultado = funcoes_2.calcular_porcentagem_pessoas_sobreviveram(titanic)
print(resultado)



"Identifique e exiba o passageiro que pagou a passagem mais cara."
passageiro_passagem_mais_cara = funcoes_2.passageiro_valor_mais_caro(titanic)
print(passageiro_passagem_mais_cara)


"Calcule e exiba a tarifa média paga pelos passageiros de cada sexo."
media_tarifa = funcoes_2.tarifa_media(titanic)
print(media_tarifa)

"Identifique e exiba a tarifa mais cara paga por passageiros de cada classe (Pclass)."




"Identifique e exiba o número total de passageiros que embarcaram em cada ponto de embarque (Embarked)."

resultado = {}
for x in titanic:
    embarked = x["Embarked"]
    if embarked == "":
        continue
    if embarked in resultado.keys():
        resultado[embarked] += 1
    else:
        resultado[embarked] = 1
print(resultado)

"Encontre e exiba o nome do passageiro mais velho a bordo."
passageiro_mais_velho = funcoes_2.pegar_passageiro_mais_velho(titanic)
print(passageiro_mais_velho)
