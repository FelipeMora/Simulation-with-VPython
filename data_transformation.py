#Crear una lista de objetos
import Sending_Data as sd
class dat:

    def __init__(self,identifier,radio_ball,pos_x,pos_y,pos_z,t_caida,v_impac,identifier_obj,collection_set):
        self.identifier = identifier
        self.radio_ball = radio_ball
        self.pos_x = pos_x#float
        self.pos_y = pos_y#float
        self.pos_z = pos_z#float
        self.t_caida = t_caida#float
        self.v_impac = v_impac#boolean
        self.ident_obj = identifier_obj
        self.goes = self.collection_to_BD(collection_set)
        self.goes(identifier_obj)

    def collection_to_BD(self,argument):
        switcher = {
            "body_data" : self.dictionary_body_data,
            "processed_info" : self.dictionary_proc_info
        }
        go = switcher.get(argument)
        return go

    def dictionary_body_data(self,argument):
        dat_general = self.body_data_general()
        print(dat_general)#Deben se enviados a sending_data
        #Leer la bd
        #sd.crud_mongo('localhost',27017,"Posicuerpos",dat_general,"body_data","r")
        sd.crud_mongo('localhost',27017,"Posicuerpos",dat_general,self.collection_set,"c")
        switcher = {
            "ball" : self.dictionary_body_data_ball,
            "wall" : self.dictionary_body_data_wall
        }
        clas_obj = switcher.get(argument)
        dat_specific = clas_obj()#problema logico
        sd.crud_mongo('localhost',27017,"Posicuerpos",dat_specific,self.collection_set,"c")
        print(dat_specific)

    def body_data_general(self):
        self.collection_set = "body_data"
        return {
            "identifier":self.identifier,
            "position_x":self.pos_x,
            "position_y":self.pos_y,
            "position_z":self.pos_z
        }

    def dictionary_body_data_ball(self):
        self.collection_set = "ball"
        return {
            "identifier": self.identifier,
            "down_time": self.t_caida,
            "impact_speed": self.v_impac
        }

    def dictionary_body_data_wall(self):#Aun no esta terminado
        self.collection_set = "ball"
        return {
            "identifier": self.identifier,
            "pending": self.t_caida,
            "angle": self.v_impac
        }

    def dictionary_proc_info(self):
        print("aun no hago nada :C")

    def to_DB_Collection(self):
        return {
            "position_x":self.nombre,
            "position_y":self.apellidos,
            "position_z": self.edad,
            "down_time":self.demarcacion,
            "impact_speed":self.internacional
        }

    def __str__(self):
        return "PosX : %x - PosY : %y - PosZ : %z - TiempoCaida : %c - VelImpacto : %v" \
            %(self.pos_x,self.pos_y,self.pos_z,self.t_caida,self.v_impac)
