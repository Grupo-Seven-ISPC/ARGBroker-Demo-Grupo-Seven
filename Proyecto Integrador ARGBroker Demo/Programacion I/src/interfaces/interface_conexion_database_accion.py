from abc import ABC,abstractmethod
class InterfaceConexionDatabaseAccion(ABC):
    @abstractmethod
    def get_accion(self):
        pass
    def get_all_acciones(self):
        pass