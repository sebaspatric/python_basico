import pprint as pp
def main():
    usuarios = listaUsuarios()
    print(usuarios)
    for usuario in usuarios:
        print(f'Usuario: {usuario}')

def listaUsuarios():
    f = open('/etc/passwd', 'r')
    datos = f.readlines()
    f.close()
    count1 = 0
    resultados = []
    for linea in datos:
        if linea[0] == '#':
            count += 1
            continue
        
    count2 = 0
    for linea in datos:
        if linea[0] == '_':
            count2 += 1
            continue
        partes = linea.split(':')  
        print(linea)
        print(partes[0])
        print(partes)
        print('--------------------------------------------------------------------')
        resultados.append(partes[0])
     
    print('lineas con #: ', count1)
    print('lineas con _: ',count2)
    print('------------------------------------------------------------------------')
    return resultados
    

if __name__ == "__main__":
    main()

