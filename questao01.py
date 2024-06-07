def maior(*numeros):
    maior_elemento = numeros[0]
    for i in range(len(numeros)):
        if numeros[i] > maior_elemento:
            maior_elemento = numeros[i]
            
    print(maior_elemento)

maior(1,2,3,4,5)
maior(4,7)
maior(100,1)
