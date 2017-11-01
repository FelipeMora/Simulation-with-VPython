#Debera realizar la conexion con la bd y realizar todoas las respectivas consultas
from pymongo import MongoClient
import time

class crud_mongo:
    #Host = localhost
    #Puerto = 27017
    #Nombre BD : Posicuerpos #user,pas
    def __init__(self,dictionary,collection_set,operation):
        self.recorrido = 0#No deberia estar aca
        self.__group = 0
        self.__dictionary = dictionary
        self.__mongoClient = MongoClient('ds235775.mlab.com',35775)
        self.db = self.__mongoClient.posicuerpos
        self.db.authenticate('Simulation','1234567')
        self.classi_operation(operation)#r
        switcher = {
            "body_data" : self.body_data,
            "processed_info" : self.proc_info,
            "ball" : self.body_data_ball,
            "wall" : self.body_data_wall,
            "grupo_general" : self.group_general
        }
        site = switcher.get(collection_set)
        site()
        self.go(collection_set)#Posible problema logico
        self.closeSession()

    def classi_operation(self,arg):
        switcher = {
            "c": self.create,
            "r": self.read
        }
        self.go = switcher.get(arg)
    #@classmethod
    def create(self,collection):#Toca clasificar la collection a la que va
        self.collection.insert(self.__dictionary)

    def body_data(self):
        self.collection = self.db.body_data

    def proc_info(self):#No esta completo
        self.collection = self.db.processed_info

    def body_data_ball(self):
        self.collection = self.db.ball

    def body_data_wall(self):
        self.collection = self.db.wall

    def group_general(self):
        self.collection = self.db.grupo_general

    def read(self,collection):
        if self.recorrido != 1:#Self recorrido podria estar en el main
            self.recorrido = 1
            try:
                self.Cursor = self.collection.find({},{"fecha":0,"_id":0}).limit(1).sort("grupo", -1)
                if self.Cursor != "NONE":
                    for fut in self.Cursor:
                        print('En for')
                        jk = fut['grupo']
                        self.__group = int(jk) + 1
                        break
            except:
                print("Hubo un problema")
            dat_group = self.group_data_general(self.__group)
            crud_mongo(dat_group,'grupo_general',"c")

    def group_data_general(self,g):
        fecha = time.strftime("%c")
        return {
            "fecha" : fecha,
            "grupo": g
        }

    def closeSession(self):
        self.__mongoClient.close()
