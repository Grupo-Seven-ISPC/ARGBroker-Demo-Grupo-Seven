import pymysql

# Clase para la conexión a la base de datos
class BaseDatos:
    def __init__(self):
        self.conexion = None
    
    def conectar(self):
        try:
            self.conexion = pymysql.connect(
                host="camila-database.cwzjkyq4owgc.us-east-1.rds.amazonaws.com",
                database="argbroker",
                user="admin",
                password="8xXnpE4d9BXXeheu2pWH"
            )
            print("Conexión exitosa")
        except pymysql.MySQLError as e:
            print(f"Error al conectar a la base de datos: {e}")

    def cerrar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada")

# Clase que representa un activo/acción
class Accion:
    def __init__(self, id_accion, nombre, simbolo, precio_compra, cantidad):
        self.id_accion = id_accion
        self.nombre = nombre
        self.simbolo = simbolo
        self.precio_compra = precio_compra
        self.cantidad = cantidad
        self.precio_actual = 0.0

    # Método para obtener el precio actual de la acción desde la tabla Cotizaciones
    def obtener_precio_actual(self, db):
        try:
            with db.conexion.cursor() as cursor:
                # Selecciona el precio de venta más reciente basado en el id_accion
                consulta = "SELECT precio_venta FROM Cotizaciones WHERE id_accion = %s LIMIT 1"
                cursor.execute(consulta, (self.id_accion,))
                resultado = cursor.fetchone()
                if resultado:
                    self.precio_actual = resultado[0]
                else:
                    print(f"No se encontró el precio actual para la acción {self.nombre}")
        except pymysql.MySQLError as e:
            print(f"Error al obtener el precio actual: {e}")

    # Método para calcular el rendimiento de la acción
    def calcular_rendimiento(self):
        if self.precio_actual > 0:
            rendimiento = ((self.precio_actual - self.precio_compra) / self.precio_compra) * 100
            return rendimiento
        else:
            return None

    # Método para mostrar los detalles y rendimiento
    def mostrar_rendimiento(self):
        rendimiento = self.calcular_rendimiento()
        if rendimiento is not None:
            print(f"---\nAcción: {self.nombre} ({self.simbolo})")
            print(f"Precio de compra: {self.precio_compra}, Precio actual: {self.precio_actual}")
            print(f"Rendimiento: {rendimiento:.2f}%")
        else:
            print(f"Precio actual no disponible para la acción {self.nombre}")

# Clase para manejar las operaciones del usuario
class Usuario:
    def __init__(self, id_usuario):
        self.id_usuario = id_usuario
        self.acciones = []

    # Método para obtener las operaciones del usuario desde las tablas Operacion y Accion
    def obtener_operaciones(self, db):
        try:
            with db.conexion.cursor() as cursor:
                consulta = """
                SELECT 
                    O.id_accion, A.nombre, A.simbolo, O.precio_unit AS precio_compra, O.cantidad
                FROM 
                    Operacion O
                JOIN 
                    Accion A ON O.id_accion = A.id_accion
                WHERE 
                    O.id_usuario = %s
                """
                cursor.execute(consulta, (self.id_usuario,))
                resultados = cursor.fetchall()

                for resultado in resultados:
                    id_accion, nombre, simbolo, precio_compra, cantidad = resultado
                    accion = Accion(id_accion, nombre, simbolo, precio_compra, cantidad)
                    self.acciones.append(accion)

        except pymysql.MySQLError as e:
            print(f"Error al obtener las operaciones del usuario: {e}")

    # Método para mostrar el rendimiento de cada acción del usuario
    def mostrar_rendimiento_acciones(self, db):
        for accion in self.acciones:
            accion.obtener_precio_actual(db)
            accion.mostrar_rendimiento()

# Función principal
def main():
    db = BaseDatos()
    db.conectar()

    try:
        id_usuario = int(input("Introduce el ID del inversor: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        return

    usuario = Usuario(id_usuario)
    usuario.obtener_operaciones(db)
    usuario.mostrar_rendimiento_acciones(db)

    db.cerrar()

if __name__ == "__main__":
    main()
