import pprint as pp
def main():
    f = open("miFichero3.txt", "w")
    lista = [
        'una linea\n',
        'dos lineas\n',
        'tres lineas\n'
    ]
       
    f.writelines(lista)
    f.close()


if __name__ == "__main__":
    main()


