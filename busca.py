#Busca Linear

import time

inicio = time.time()
frase = "Não atire o pau no gato Porque isso Não se faz O gatinho É nosso amigo Não devemos maltratar os animais Jamais"
frase = frase.lower().split()
contador = 0

print ("Busca Linear")

for i in frase:
    with open(r"c:\Users\Joel\Desktop\Estudos\Univates\atividade\lista.txt", encoding="utf8") as arquivo: #Caminho completo do arquivo a ser lido
        for linha in arquivo:
            if frase[contador] in linha.strip().split():
                continue
    contador = contador + 1

final = time.time() - inicio #Calcula o tempo

print("Tempo: ", final)
