import pandas as pd
import nltk as nk
import matplotlib.pyplot as plt
import wordcloud as wd
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

pergunta = int(input('Qual texto você quer analisar? 1: Alice in Wonderland, 2: Through the Looking Glass ou 3: War and Peace '))
if pergunta == 1: 
    # Abre o arquivo
    f = open('AliceInWonderland.txt', encoding='utf8')
    raw = f.read() # Le o conteudo do arquivo
elif pergunta == 2: 
    g = open('ThroughTheLookingGlass.txt', encoding='utf8')
    raw = g.read()
else: 
    h = open('WarAndPeace.txt', encoding='utf8')
    raw = h.read()

# Cria um tokenizer que mantem somente palavras
tokenizer = nk.tokenize.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(raw)
# A variavel 'tokens' eh uma lista de tokens transformando todos os tokens em letras minusculas.
lwords = []
for word in tokens:
    lwords.append(word.lower())
    # lwords agora so contem tokens com letras minusculas
    #
    # carrega as stopwords da lingua Inglesa em sw
sw = nk.corpus.stopwords.words('english') #filtragem
words_ns = []
for word in lwords:
    if word not in sw:
        words_ns.append(word)

dicfreq = {
'a':{}, 'b':{}, 'c':{}, 'd':{}, 'e':{}, 'f':{}, 'g':{}, 'h':{}, 'i':{}, 'j':{}, 'k':{}, 'l':{}, 'm':{}, 'n':{}, 'o':{}, 'p':{}, 'q':{}, 
'r':{}, 's':{}, 't':{}, 'u':{}, 'v':{}, 'w':{}, 'x':{}, 'y':{}, 'z':{} 
}

count = 0 
temp = 0
for i in words_ns: #procura palavra em words_ns
    elem = 'a' 
    for elem in dicfreq:
        if words_ns[temp][0] == elem: #se a primeira letra da palavra for o elem 
            if words_ns[temp] in dicfreq[elem]: #se essa palavra já existir no discionario criado
                count = dicfreq[elem][words_ns[temp]] 
                count = count + 1
                dicfreq[elem][words_ns[temp]] = count
            else: 
                dicfreq[elem].update([(words_ns[temp], 1)])
        elem_iterada = ord(elem)+1
        elem = chr(elem_iterada) #soh muda de letra se o 'elem' nao for igual a 'words_ns[temp][0]' 
    temp = temp +1

lwocorrencias = []
for i in range (ord('a'), ord('z')+1): #Loop para acessar letras a até z.
    dicfreq_elem = dicfreq[chr(i)] #Acessa o dicionário de cada uma das letras.
    palavras_lista = list(dicfreq_elem.keys()) #palavras_lista armazena, em forma de lista, todos os valores de cada uma das chaves do dicionario.
    for j in palavras_lista: #varre todos os elementos de palavras_lista.
        nao_ord = dicfreq[chr(i)].popitem() #armazena em uma lista nao ordenada.
        lwocorrencias.append(nao_ord)
#print(nao_ord)

def insertionSort(lista):  
    for i in range(1, len(lista)): 
        key = lista[i] 
        j = i-1
        while j >= 0 and key[1] > lista[j][1] : #Acessa apenas o numero de ocorrencias
                lista[j + 1] = lista[j] 
                j -= 1
        lista[j + 1] = key
insertionSort(lwocorrencias)

#Gerar o código em barras
freqword=pd.DataFrame.from_records(lwocorrencias[:20],columns=['word','count'])
freqword.plot(kind='bar',x='word')

#Gerar o wordcloud
freq_palavra = dict(lwocorrencias[:20])
wordc = wd.WordCloud(width=900,height=500, max_words=20, relative_scaling=1,normalize_plurals=False).generate_from_frequencies(freq_palavra)


plt.figure()
plt.imshow(wordc, interpolation='bilinear')
plt.axis("off")
plt.show()
