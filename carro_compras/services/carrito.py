from flask import jsonify

# Creacion de la clase Producto donde se definen los campos de ingreso.
class Producto:
    def __init__(self,id_producto,nombre,precio,stock,cantidad):
        self.id_producto = int(id_producto)
        self.nombre = str(nombre)
        self.precio = float(precio)
        self.stock = int(stock)
        self.cantidad = int(cantidad)


# Creacion del carrito
class CarritoCompra:
    def __init__(self):
        self.carrito = [] # Inicio de ina lista que funcionara como el carrito.

    # Ingreso de elementos a la lista.
    def add_items(self,producto):
        self.carrito.append(producto)


    # Muestra de productos de la lista, se usa una lista de diccionarios intermedia para mostrar los productos.
    def show_item(self):
        try:
            muestra_productos = []
            for products in self.carrito:
                muestra_productos.append({'id_producto' : products.id_producto,'nombre' : products.nombre,'precio' : products.precio,'stock' : products.stock,'cantidad' : products.cantidad})
            return jsonify({'Carrito' : f'{muestra_productos}'}),200
        except Exception as error:
            return jsonify({'Error' : f'error en mostrar el carrito : {error}'}),400


    # Remocion de un solo elemento de la lista.
    def remove_item(self,producto):
        try:
            for products in self.carrito[:]:
                if products.nombre == producto:
                    self.carrito.remove(products)
                    return jsonify({'Mensaje' : f'Producto {products} eliminado con exito.'}),200
            else:
                return jsonify({'Mensaje' : f'Producto {products} no encontrado.'}),200
        except Exception as error:
            return jsonify({'Error' : f'Error en la eliminacion del producto : {error}'})


    # Eliminacion de todos los elementos de la lista.
    def clear_cart(self):
        self.carrito.clear()
        return jsonify({'Mensaje' : 'carrito vacio.'}),200