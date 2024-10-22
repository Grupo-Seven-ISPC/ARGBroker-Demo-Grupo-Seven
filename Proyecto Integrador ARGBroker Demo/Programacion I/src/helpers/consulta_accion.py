import yfinance as yf

class ConsultaAccion:
    def __init__(self,accion_a_consultar):
        self.__accion_a_consultar=yf.Ticker(accion_a_consultar)

    def get_accion_a_consultar(self):
        return self.__accion_a_consultar
    def set_accion_a_consultar(self,nuevo_valor):
        self.__accion_a_consultar=yf.Ticker(nuevo_valor)

    def get_info_accion(self):
        return self.__accion_a_consultar.info
    
    def get_precio_apertura(self):
        info = self.get_info_accion()
        return info.get('open', 'Precio de apertura no disponible')

    def get_precio_actual(self):
        info = self.get_info_accion()
        return info.get('regularMarketPrice', 'Precio actual no disponible')

    def get_precio_cierre_anterior(self):
        info = self.get_info_accion()
        return info.get('previousClose', 'Precio de cierre anterior no disponible')
    
    def get_precio_compra(self):
        info = self.get_info_accion()
        return info.get('bid', 'Precio de compra (Bid) no disponible')
    def get_precio_venta(self):
        info = self.get_info_accion()
        return info.get('ask', 'Precio de venta (Ask) no disponible')
    def get_cantidad_acciones_totales_en_el_mercado(self): 
        info = self.get_info_accion()
        return info.get('sharesOutstanding', 'No disponible')
    def get_cantidad_acciones_totales_disponibles_en_el_mercado_compra_venta(self):
        info = self.get_info_accion()
        return info.get('floatShares', 'No disponible')
    def validar_acciones_disponibles_mercado(self,cantidadRequerida):
        cantidad_acciones_disponibles=self.get_cantidad_acciones_totales_disponibles_en_el_mercado_compra_venta()
        if cantidad_acciones_disponibles >=cantidadRequerida:
            print("Cantidad de Acciones para compra/venta existente y disponible")
            return True
        else:
            print("Cantidad requerida excede la cantidad disponible de acciones disponibles")
            return False

    

def prueba():
    ypf=ConsultaAccion("YPFD.BA")
    print(ypf.get_precio_actual())
    print(ypf.get_precio_apertura())
    print(ypf.get_precio_cierre_anterior())
    print(ypf.get_precio_compra())
    print(ypf.get_precio_venta())

prueba()