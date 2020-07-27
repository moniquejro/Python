#Aqui vamos aprender operações com string

frase = 'Curso em vídeo Python'
print(frase)

print('A quarta letra é: {}.'.format(frase[3])) #vai mostrar a quarta letra
print('Da quarta letra até a letra treze: {}.'.format(frase[3:13]))
print('Do início até a letra treze: {}.'.format(frase[:13])) #note a diferença dos números entre [ ]
print('Da letra treze até o final: {}.'.format(frase[13:]))
print('Da primeira letra até a décima quinta: {}.'.format(frase[1:15:2])) #o (:2) significa o pulo, o passo da contagem
print('Da primeira letra até a décima quinta: {}.'.format(frase[1::2])) #aqui é quando não sabemos o final, mas delimitamos o passo
print('Da primeira letra até a décima quinta: {}.'.format(frase[::2])) #aqui é quando queremos a string inteira e de quanto em quanto irá caminhar

#Para pular uma linha é só fazer como o exemplo abaixo:

print('\n')
#Também pode ser adicionado em meio ao texto

#Se eu quiser mostrar um texto de muitas linhas, é só
#eu adicionar 3 aspas no início e no final, assim:

print("""Nossa missão é apoiar jovens a construírem 
carreiras sustentáveis e prósperas e fornecer aos empregadores 
uma rede de talentos altamente qualificados e motivados, 
visando aprimorar os resultados de seus negócios.""")
print('\n')
#Aqui a 'frase' é uma cadeia de caracter, mas em python tudo é um objeto.

print(frase.count('o'))
print('Acima contou quantas vezes a letra "o" \napareceu na frase: Curso em vídeo.')
print('Lembrando que letras maiusculas e minusculas NÃO são as mesmas coisas.')

print('\nAqui vamos primeiro jogar a frase toda para letra maiuscula \ne depois contar quantas letras "O" contém na frase. Possui {}'.format(frase.upper().count('O')))

print('\nA frase possui {} caracter CONTANDO COM ESPAÇO.'.format(len(frase))) #Saber quantas letras possui na frase.

print('\nA frase possui {} letras.'.format(len(frase.strip()))) #Retirando os espaços com strip

print('\nSubstituindo a palavra Python por Android. \n-->{}'.format(frase.replace('Python', 'Android')))

print(frase[0]) #Mostra a primeira letra da frase.

#Em frase[0] = 'J'
#Deveria acontecer a substituição, porém não é permitido a troca de objetos em vetores.
#O comando REPLACE substitui, mas não salva a troca.
#Tente aí:

frase.replace('Python', 'Android')
#vai acontecer a troca, mas se você chamar a frase, ela vai mostrar o que?
print('A frase base é: {}'.format(frase))

#Se você fizer: frase = frase.replace('Python', 'Android') aí sim vai substituir.

print('Curso' in frase) #conferindo se 'Curso' está em frase. Vai retornar true or false

print(frase.find('Curso')) #Vai encontrar na posição 0
print(frase.find('curso')) #Vai devolver um valor negativo porque não existe em letra minuscula
print(frase.lower().find('curso')) #Jogando a frase toda para minusculo é possivel encontrar a palavra
print(frase.split()) #Cria uma lista, separado por espaço
dividido = frase.split()
print(dividido[0]) #mostra o ítem 0 da lista
print(dividido[2][3]) #No ítem 2, vai mostrar a terceira letra
