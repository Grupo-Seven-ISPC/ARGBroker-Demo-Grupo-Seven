from src.database.conexion_database import DatabaseConnection
from src.database.conexion_usuario import ConexionDatabaseUsuario
from src.database.conexion_movimiento import ConexionDatabaseMovimiento
from src.database.conexion_accion import ConexionDatabaseAccion
from src.database.conexion_operacion import ConexionDatabaseOperacion
from src.helpers.validaciones import Validaciones
from src.helpers.helper_password import HelperPassword
from src.helpers.helper_usuario import HelperUsuario
from src.helpers.helper_transaccion import HelperTransaccion
from src.helpers.helper_programa import HelperPrograma
from src.helpers.helper_stock import HelperStock
from src.service.auth_service import AuthService
from src.service.password_service import PasswordService
from src.service.stock_service import StockService
from src.service.user_service import UserService
from src.service.programa_service import ProgramaService

if __name__ == "__main__":
    database=DatabaseConnection()
    conexion_usuario_db=ConexionDatabaseUsuario(database)
    conexion_movimiento_db=ConexionDatabaseMovimiento(database)
    conexion_accion_db=ConexionDatabaseAccion(database)
    conexion_operacion_db=ConexionDatabaseOperacion(database)

    validaciones=Validaciones(conexion_usuario_db)
    helper_password= HelperPassword()
    helper_transaccion=HelperTransaccion()
    helper_usuario=HelperUsuario(validaciones)
    helper_programa=HelperPrograma()
    helper_stock=HelperStock(conexion_accion_db,helper_transaccion,validaciones,conexion_movimiento_db,conexion_operacion_db)

    auth_service=AuthService(helper_usuario,conexion_usuario_db,conexion_movimiento_db)
    password_service=PasswordService(conexion_usuario_db,helper_password,validaciones,auth_service)
    stock_service=StockService(helper_stock)
    user_service=UserService(conexion_movimiento_db,stock_service)
    programa_service=ProgramaService(auth_service,password_service,stock_service,user_service,helper_programa)

    app=programa_service
    app.start_program()