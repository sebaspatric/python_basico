import pprint as pp
def main():
    fichero = 'miFichero4.txt'
    lista = [
        'una linea\n',
        'dos lineas',
        'tres lineas'
    ]
    escribe(fichero, lista)


       
def escribe(fichero, datos):
    f = open(fichero, "w")
    
    for linea in datos:
        salto = linea.endswith('\n')
        #print(type(salto))
        print("linea sin \\n", salto, linea)
        if not salto:
            linea += '\n'
        f.write(linea)
    f.close()



if __name__ == "__main__":
    main()


