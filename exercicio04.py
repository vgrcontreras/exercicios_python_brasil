# 4) Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

nota1 = float(input('Digite a nota do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
nota3 = float(input('Digite a nota do terceiro bimestre: '))
nota4 = float(input('Digite a nota do quarto bimestre: ')) 

notas.append(nota1)
notas.append(nota2)
notas.append(nota3)
notas.append(nota4)

media = sum(notas) / len(notas)

print(f'A média das notas é {media}')