#composicion
#una clase tiene una o más instancias de otra


class Categorias:
    idCategoria = 0
    NombreCategoria = ""

class Proveedores:
    idProveedor = 0
    nombreProveedor = ""
    direccion = ""
    telefono = ""
    codPostal = ""

class Productos:
    idProducto = 0
    CategoriaProducto = Categorias()
    Precio = 0
    Tamaño = 0
    TipoDeProducto = 0
    CIFProveedor = Proveedores()

p = Productos()
p.CIFProveedor.nombreProveedor
print(p)
print(p.CIFProveedor.nombreProveedor)
p.CIFProveedor.nombreProveedor = "Juan"
print(p.CIFProveedor.nombreProveedor)
p.CategoriaProducto.idCategoria
print(p.CategoriaProducto.idCategoria)