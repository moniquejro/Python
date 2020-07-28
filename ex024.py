#Crie um programa que leia o nome de uma cidade
#e diga se começa ou não com "SÃO"

cid = str(input('Em que cidade você mora? ')).strip()
print(cid[:3].upper() == "SÃO")
