from abc import ABC,abstractmethod  
class InterfaceConexionDatabaseMovimiento(ABC):
    @abstractmethod
    def registrar_ingreso(self,monto,id):
        pass
    @abstractmethod
    def registrar_egreso(self,monto,id):
        pass
    @abstractmethod
    def calcular_saldo(self):
        pass
    @abstractmethod
    def save_changes(self):
        pass