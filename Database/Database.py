import mysql.connector


class DataBase:
    
    def __init__(self):

        self.__user="root"
        self.__password=""
        self.__host="localhost"
        self.__database="prueba2"
    
    @property
    def user(self):
        return(self.__user)
    
    @property
    def password(self):
        return(self.__password)
    
    @property
    def host(self):
        return(self.__host)
    
    @property
    def database(self):
        return(self.__database)
    
    def conectarBD(self):
        try:
        
            cnx=mysql.connector.connect(

                user=self.user, 
                password=self.password,
                host=self.host,
                database=self.database
            )
            print("exito en la conexion con BD")
            cnx.close()
        except mysql.connector.Error as err:
            print(format(err))
