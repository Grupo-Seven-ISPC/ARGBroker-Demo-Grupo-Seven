from abc import ABC,abstractmethod  
class InterfaceConexionDatabaseUsuario(ABC):
    @abstractmethod
    def add(self,objeto):
        pass
    @abstractmethod
    def update(self,columna_a_actualizar, nuevo_valor, condicion_columna, condicion_valor):
        pass
    @abstractmethod
    def get_one(self,atributo):
        pass
    @abstractmethod
    def save_changes(self):
        pass