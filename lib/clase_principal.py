import pymysql
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth

	
class ppal:
    def __init__(self, id_cliente, id_local):
        print('amda?')
        self.id_cliente = id_cliente
        self.id_local = id_local
        conexion_datos = self.obtener_conexion()
        self.obtener_conexion()
        self.obterner_lista()

    def obtener_conexion(self):
        self.host ='localhost'
        self.user ='andi'
        self.password ='andi123'
        self.database ='mlxtend'

    def obterner_lista(self):
        try:
            db = pymysql.connect(
			host = self.host,
			user = self.user,
			password = self.password,
			database = self.database
            )
            #TODO: Borrar esta linea
            self.id_cliente = 273
            self.id_local = 42
            db_cursor = db.cursor()
            
            #Buscamos las transacciones/productos
            query = """
                SELECT
                    GROUP_CONCAT(DISTINCT f.id_familia) productos
                FROM
                    pedido_articulo pa
                JOIN    pedido p USING (id_pedido)
                JOIN    articulo a USING (cod_interno)
                JOIN    familia f USING (id_familia)
                WHERE
                        p.id_cliente = %s
                AND     p.id_local = %s
                GROUP BY p.id_pedido
                LIMIT 2
                
                ;"""
            execute = db_cursor.execute(query, (self.id_cliente, self.id_local))
            print(" LA exceute ",execute, '\n')
            # print(db_cursor.fetchall(), '\n')
            # row = db_cursor.fetchone()
            # while row is not None:
            #     for r in row:
            #         print(r)
            #     row = db_cursor.fetchone()
            te = TransactionEncoder()
            dataset = []
            row = db_cursor.fetchone()
            print(row)
            e = ''
            while row is not None:
                data_aux = []
                for elem in row[0]:
                    if(elem != ','):
                        e = e + elem
                    else:
                        data_aux.insert(len(data_aux),int(e))
                        e = ''
                e = ''
                dataset.insert(len(dataset),data_aux)
                row = db_cursor.fetchone()
            print(dataset)
            te_ary = te.fit(dataset).transform(dataset)
            df = pd.DataFrame(te_ary, columns=te.columns_)
            pd.set_option("display.max_rows", None, "display.max_columns", None)
            print(df)
            fpg = fpgrowth(df, min_support=0.6)
            print(fpg)
        except Exception as e:
            print(e)
            exit(-1)
        finally:
            db.close()
            db_cursor.close()
