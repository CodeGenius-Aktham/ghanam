# Importacion de los servicios del carrito. 
from flask import Blueprint,request, jsonify
from carro_compras.services.carrito import Producto, CarritoCompra

# Uso del Blueprint para armar la modularidad.
carrito_compras = Blueprint('compras',__name__)

# Inicio del carrito vacio.
mi_carrito = CarritoCompra() 

# Rutas necesarias (GET,POST,PUT,DELETE)

# Muestra de los productos del carrito.
@carrito_compras.route('/show',methods = ['GET'])
def obtener_carrito():
    return mi_carrito.show_item()


# Ingreso de los productos al carrito.
@carrito_compras.route('/income',methods = ['POST'])
def subir_productos():
    data = request.get_json()
    productos = Producto(data.get('id_producto'),data.get('nombre'),data.get('precio'),data.get('stock'),data.get('cantidad'))
    mi_carrito.add_items(productos)
    return jsonify({'Mensaje' : 'Producto añadido con exito'}),200


# Eliminacion de productos.
@carrito_compras.route('/clear_item',methods=['PUT'])
def eliminar_producto_carrito():
    data = request.get_json()
    mi_carrito.remove_item(data.get('nombre'))
    return jsonify({'Mensaje' : 'producto eliminado con exito.'}),200


# Eliminacion de todos los productos del carrito.
@carrito_compras.route('/clear',methods=['DELETE'])
def eliminar_todo_el_carrito():
    return mi_carrito.clear_cart()