from abc import ABC,abstractmethod  
class InterfaceConexionDatabaseUsuario(ABC):
    @abstractmethod
    def add(self,objeto):
        pass
    def update(self,columna_a_actualizar, nuevo_valor, condicion_columna, condicion_valor):
        pass
    def get_one(self,atributo):
        pass
    def save_changes(self):
        pass