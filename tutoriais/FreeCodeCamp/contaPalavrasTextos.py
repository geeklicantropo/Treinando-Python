fname = input('Enter the file: ')
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.strip()
    for w in wds:
        #Se a palavra existir no dicionário, adicionamos o valor padrão 0 e somamos + 1
        di[w] = di.get(w,0) + 1


largest = -1
theword = None
for key, value in di.items():
    print(key,value)
    if value > largest:
        largest = value
        theword = key

print(theword, largest)