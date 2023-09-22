from random import randint

data = ["data0.txt","data1.txt","data2.txt","data3.txt","data4.txt"] # cria um númoro randomico para selecionar um dos arquivos txt

with open(data[randint(0,4)], "r") as arquivo:
    linhas = arquivo.readlines()

opResult = []

try:
    num_iteracoes = int(linhas[0].strip())

    opIndex = 1 # Indice de operação para leitura das linhas do arquivo
    for i in range(num_iteracoes):
        op = linhas[opIndex].strip() # tira os espaços em branco das linhas selecionadas pelo opIndex
        
        # Seleciona os valores de cada linha especifica do arquivo txt baseado no opIndex, para separar os conjuntos 1 e 2 
        arrayA = set(map(str.strip, linhas[opIndex + 1].split(','))) 
        arrayB = set(map(str.strip, linhas[opIndex + 2].split(',')))
        
        if op == 'U':
            result = arrayA.union(arrayB)
            opDescription = "União"
        elif op == 'I':
            result = arrayA.intersection(arrayB)
            opDescription = "Interseção"
        elif op == 'D':
            result = arrayA.difference(arrayB)
            opDescription = "Diferença"
        elif op == 'C':
            result = {(x, y) for x in arrayA for y in arrayB}

            opDescription = "Produto Cartesiano"
        
        opResult.append(f"{opDescription}:\nConjunto 1 - {arrayA}\nConjunto 2 - {arrayB}\nResultado: - {result} \n")
        
        opIndex += 3
except ValueError:
    print("BIG Andrey fez caquinha...")

for line in opResult:
    print(line)