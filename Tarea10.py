matrix = [[9, 4, 11], [88, 64, 23], [8, 51, 87]]
print("elementos de la matriz")
print(f"{matrix[0]} \n{matrix[1]} \n{matrix[2]}")
print("Buscar el numero 87 en la matriz")
valor = 87


def buscar_valor(matrix, valor):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == valor:
                return f"El valor {valor} se encontro en la posicion ({i},{j}) de la matriz."
    return f"El valor {valor} no se encontro en la nmatriz."


valor_buscado = 87
resultado_busqueda = buscar_valor(matrix, valor_buscado)
print(resultado_busqueda)
matrix= [9, 4, 11, 88, 64, 23, 8, 51, 87]
def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

print("matriz en orden ascendente")
print(sort(matrix))