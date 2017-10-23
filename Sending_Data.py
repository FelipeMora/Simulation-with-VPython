#Debera realizar la conexion con la bd y realizar todoas las respectivas consultas
from pymongo import MongoClient


class crud_mongo:
    #Host = localhost
    #Puerto = 27017
    #Nombre BD : Posicuerpos
    def __init__(self,host,puerto,bd):
        print("Hola llegue aca :V")
        self.__mongoClient = MongoClient()
        self.db = self.__mongoClient.bd

    def create(self,collection,dictionary):
        collection = self.bd.collection#Indicara en que collecion desea
        #collection.insert()
        #Debe recibir los objetos ya pasados a diccionaris

    def read(self):
        print("Aun no se leer la BD, lo siento :C")


    def closeSession(self):
        self.mongoCliente.close()
