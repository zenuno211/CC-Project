import re

f = open('trees.csv')
firstLine = f.readline()

#determina se o separador é ',' ou ';'
separator = re.search(r'[,;]',firstLine).group(0)

#determina os campos da primeira linha
firstLineCampos = re.split(separator,firstLine)
#tuplo com nome do campo e informação sobre tipo
campos = []
#inicializar campos com primeira linha
for campo in firstLineCampos:
    campo = campo.strip()
    campo = re.sub(r'"',r'',campo)
    split = re.split(r'\*',campo)

    if len(split) == 2:
        if split[1] != '': #nome do campo alterado se for avg/min/max/sum
            campos.append((split[0]+'_'+split[1], split[1]))
        else:
            campos.append((split[0], split[1]))
    else: 
        campos.append((split[0],None))

print('[\n\t{')

numCompile = re.compile(r'^[\-+]?([1-9]\d*|0)([\.\,]\d+)?([eE][+\-]\d+)?$')
boolCompile = re.compile(r'^[Tt]rue|[Ff]alse$')

for i, line in enumerate(f): #ler restantes linhas
    if i != 0:
        print('\t},\n\t{')
    valores = re.split(separator,line)

    for index, valor in enumerate(valores):                                   
        valor = valor.strip()
        title, option = campos[index]
        
        print('\t\t\"'+title+ '\":',end=' ')

        if index == len(campos)-1:
            lastField = True
        else:
            lastField = False
        if option == None:
            valor = re.sub(r'"',r'',valor)
            isNumber = numCompile.search(valor)
            isBool = boolCompile.search(valor)
            if isNumber != None or isBool != None:
                print(valor, end='')
            else:
                print('"' + valor + '"', end='')

            if not(lastField):
                print(',')
            else:
                print()
            
        else:
            valor = valor[1:-1] #excluir parentesis
            lista = re.split(r',',valor)
            
            # executa as funções avg/min/sum/max caso seja necessário
            if option == 'avg':
                listResult = False
                lista = list(map(float, lista))
                value = round(sum(lista)/len(lista),2)
            elif option == 'min':
                listResult = False
                lista = list(map(float, lista))
                value = round(min(lista),2)
            elif option == 'sum':
                listResult = False
                lista = list(map(float, lista))
                value = round(sum(lista),2)
            elif option == 'max':
                listResult = False
                lista = list(map(float, lista))
                value = round(max(lista),2)
            else:
                listResult = True
            if listResult:
                print('[',end='')
                isNumber = numCompile.search(lista[0])
                isBool = boolCompile.search(lista[0])
                if isNumber != None or isBool != None:
                    for index, item in enumerate(lista):
                        item = re.sub(r'"',r'',item)
                        if index > 0:
                            print(',' ,end='')
                        print(item,end='')
                else:
                    for index, item in enumerate(lista):
                        item = re.sub(r'"',r'',item)
                        if index > 0:
                            print(',' ,end='')
                        print('"' + item + '"' ,end='')
                print(']',end='')
            else:
                print(value,end='')

            if not(lastField):
                print(',')
            else:
                print('')
        
print('\t}\n]')