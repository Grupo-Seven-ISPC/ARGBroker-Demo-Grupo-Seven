from abc import ABC,abstractmethod
class InterfaceConexionDatabaseCotizaciones(ABC):
    @abstractmethod
    def consultar_simbolo_compra(self,simbolo):
        pass
    @abstractmethod
    def consultar_simbolo_venta(self,simbolo):
        pass