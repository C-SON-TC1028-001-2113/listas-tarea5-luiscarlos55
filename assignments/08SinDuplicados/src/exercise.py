def main():
    #escribe tu código abajo de esta línea
    a = int(input())
    elementos = []
    i = 0
    if a>=0 :
        while i<a :
            valor = input()
            elementos.append(valor)
            i = i+1
        print(elementos)
        duplicados = []
        for i in elementos :
            if i not in duplicados :
                duplicados.append(i)
        print(duplicados)
    else:
        print('Error')

    pass

if __name__=='__main__':
    main()
