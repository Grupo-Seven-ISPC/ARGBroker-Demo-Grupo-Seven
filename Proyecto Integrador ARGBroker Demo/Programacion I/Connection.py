import mysql.connector

connection = mysql.connector.connect(
        host='autorack.proxy.rlwy.net',
        port=36032,
        user='root',
        password='auFehhmMzBYwWmHVZGsTQmFzQzRwHTfh',
        database='argbroker'
    )
class ConexionDatabase:
    def __init__(self):
        self.connection=connection
    
    def get_connection(self):
        return self.connection

    def save_changes(self):
        self.connection.commit()

    def add_to_database(self, tabla, objeto):
        cursor = self.connection.cursor()
        if isinstance(objeto, dict):  #Si el objeto ya es un diccionario se deja asi si no se lo convierte en diccionario
            objeto_final = objeto
        else:
            objeto_final = objeto.__dict__
        columnas = ', '.join(objeto_final.keys())
        valores = list(objeto_final.values())
        placeholders = ', '.join(['%s'] * len(valores))
        insert_query = f"""
        INSERT INTO {tabla} ({columnas}) 
        VALUES ({placeholders})
        """
        cursor.execute(insert_query, valores)
        self.save_changes()
        print(f"Datos insertados en la tabla {tabla}")
    
    def search_one_in_database(self,tabla,columnas,valores):
        cursor = self.connection.cursor()
        where_clause = ' OR '.join([f"{columna} = %s" for columna in columnas])
        query = f"""
        SELECT * FROM {tabla} WHERE {where_clause}
        """
        cursor.execute(query,valores)
        resultado = cursor.fetchone() 
        return resultado
    def search_in_database(self, tabla, columnas, valores):
        cursor = self.connection.cursor()
        where_clause = ' OR '.join([f"{columna} = %s" for columna in columnas])
        query = f"""
        SELECT * FROM {tabla} WHERE {where_clause}
        """
        cursor.execute(query, valores)
        resultados = cursor.fetchall()
        return resultados

    
    def update_one_column(self, tabla, columna_a_actualizar, nuevo_valor, condicion_columna, condicion_valor):
        cursor = self.connection.cursor()
        query = f"""
        UPDATE {tabla}
        SET {columna_a_actualizar} = %s
        WHERE {condicion_columna} = %s
        """
        cursor.execute(query, (nuevo_valor, condicion_valor))
        self.save_changes()