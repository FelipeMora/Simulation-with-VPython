#Debera realizar la conexion con la bd y realizar todoas las respectivas consultas
from pymongo import MongoClient


class crud_mongo:
    #Host = localhost
    #Puerto = 27017
    #Nombre BD : Posicuerpos
    def __init__(self,host,puerto,bd,dictionary,collection_set,operation):
        print(">>>>>>>>>>")*20
        self.__dictionary = dictionary
        self.__mongoClient = MongoClient()
        self.db = self.__mongoClient.bd
        self.classi_operation(operation)
        self.go(collection_set)#Posible problema logico

    def classi_operation(self,arg):
        switcher = {
            "c": self.create,
            "r": self.read
        }
        self.go = switcher.get(arg)
    #@classmethod
    def create(self,collection):#Toca clasificar la collection a la que va
        switcher = {
            "body_data" : self.create_body_data,
            "processed_info" : self.create_proc_info,
            "ball" : self.create_body_data_ball,
            "wall" : self.create_body_data_wall
        }
        site = switcher.get(collection)
        print("-<>-<> | " + str(site))*30
        collection_cla = site()
        collection_cla.insert(self.__dictionary)
        print("///////// LO HE CREADO >>>>>>>>>>>>>>>>")*30
        self.closeSession()

    def create_body_data(self):
        collection = self.db.body_data
        return collection

    def create_proc_info(self):#No esta completo
        collection = self.db.processed_info
        return collection

    def create_body_data_ball(self):
        print("------------> EN BALL <---------------")
        collection = self.db.ball
        return collection

    def create_body_data_wall(self):
        collection = self.db.wall
        return collection

    def read(self):
        print("Aun no se leer la BD, lo siento :C")

    def closeSession(self):
        self.__mongoClient.close()
