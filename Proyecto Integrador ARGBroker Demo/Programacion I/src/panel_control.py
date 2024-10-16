# Simulación de un saldo inicial para el usuario
saldo_inicial = 1000000

# Función para mostrar el panel de control
def mostrar_panel_de_control():
    print("\n--- Panel de Control ---")
    print(f"Saldo actual: ${saldo_inicial:,}")  # Muestra el saldo formateado con comas
    print("------------------------")

# Flujo principal para mostrar el panel de control
if __name__ == "__main__":
    while True:
        print("\n1. Ver saldo")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_panel_de_control()
        elif opcion == "2":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
