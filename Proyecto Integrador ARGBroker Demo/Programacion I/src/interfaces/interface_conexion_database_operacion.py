from abc import ABC,abstractmethod
class InterfaceConexionDatabaseOperacion(ABC):
    @abstractmethod
    def get_operacion(self,id):
        pass
    @abstractmethod
    def get_operaciones(self,id):
        pass
    @abstractmethod
    def add_operacion(self,id_operacion,id_estado,id_usuario_id_accion):
        pass
    @abstractmethod
    def save_changes(self):
        pass