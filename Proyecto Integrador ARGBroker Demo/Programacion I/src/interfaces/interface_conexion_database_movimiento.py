from abc import ABC,abstractmethod  
class InterfaceConexionDatabaseMovimiento(ABC):
    @abstractmethod
    def registrar_ingreso(self,monto,id):
        pass
    def registrar_egreso(self,monto,id):
        pass
    def calcular_saldo(self):
        pass
    def save_changes(self):
        pass