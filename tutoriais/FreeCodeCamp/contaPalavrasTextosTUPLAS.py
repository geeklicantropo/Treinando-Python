fname = input('Enter the file: ')
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.strip()
    for w in wds:
        #Se a palavra existir no dicionário, adicionamos o valor padrão 0 e somamos + 1
        di[w] = di.get(w,0) + 1

print(di)

tmp = list()
for k,v in di.items():
    #Cria uma nova lista, dessa vez por valor/chave e não por chave/valor.
    #O objetivo é pegar o valor correspondente ao número de vezes que uma palavra apareceu
    #no texto e ordená-lo para pegar o maior número
    newt = (v,k)
    tmp.append(newt)

#Ordena uma tupla pela chave(k). Só que como a key corresponde ao valor depois de ter sido
#trocado de ordem - (k,v) virou (v,k) - a ordenação será feita pelo valor e não pela chave
#Reverse é importante porque ele vai ordenar do maior para o menor. E queremos pegar somente os maiores
tmp = sorted(tmp, reverse=True)

#Printa as 5 palavras que repetem mais vezes, mas já troca novamente pelo seu par chave/valor
for v,k in tmp[:5]:
    print(k,v)