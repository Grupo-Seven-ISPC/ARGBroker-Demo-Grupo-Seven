class HelperPrograma:
    def opciones_programa_principal(self,primera_vez,funcion_cambiar_primera_vez):
        if primera_vez():
            print("Bienvenido al sistema.")
            funcion_cambiar_primera_vez(False)
        print("\n1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Olvido su contraseña?")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion
     
    def opciones_dashboard(self):
        print("\n1. Ver saldo actual")
        print("2. Historial Transacciones")
        print("3. Rendimientos")
        print("4. Registrar ingreso")
        print("5. Registrar egreso")
        print("6. Mostrar precio de compras y ventas")
        print("7. Comprar/Vender Acciones")
        print("8. Cerrar sesión")
        opcion_usuario = input("Seleccione una opción: ")
        return opcion_usuario
    