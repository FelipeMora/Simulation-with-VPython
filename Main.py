from pymongo import MongoClient
import Use_VPython as uv
import Sending_Data as sd

def ant_main(msg):
    print(msg)
    print("=")*800
    main()

class main:

    def __init__(self):
        uv.simulation()
        #sd.crud_mongo('localhost',27017,"Posicuerpos")

    def sent_dat(self,h,r,t):
        print("Debe enviar la informacion")

if __name__ == '__main__':
    msg = "Iniciando proceso"
    ant_main(msg)
##Debe recibir informacion seguidamente de Use_VPython
#Posicion vectorial del objeto
#Angulo de inclinacion del plano


#Despues de recibirla debe enviarla a data_transformation para pasarla a Sending_Data
#Cada return de data_transformation debe pertenecer a una lista de objetos


#Se debe buscar datos en la bd que tengan relacion con los datos que se reciban en cada instante
#de este modo se evitara hacer procesos innecesarios lo que llevara a tener un mayor tiempo para tomar la decision
