from abc import ABC,abstractmethod
class InterfaceConexionDatabaseAccion(ABC):
    @abstractmethod
    def get_accion(self,id):
        pass
    @abstractmethod
    def get_all_acciones(self):
        pass
    @abstractmethod
    def get_cantidad_acciones_disponibles(self,simbolo):
        pass
    @abstractmethod
    def disminuir_cantidad_acciones(self,cantidad,simbolo):
        pass
    @abstractmethod
    def aumentar_cantidad_acciones(self,cantidad,simbolo):
        pass
    @abstractmethod
    def get_cantidad_acciones_adquiridas_usuario(self,id):
        pass
    @abstractmethod
    def get_cantidad_acciones_adquiridas_usuario_por_simbolo(self,id_usuario,simbolo):
        pass