#Crear una lista de objetos
class dat:

    def __init__(self,pos_x,pos_y,pos_z,t_caida,v_impac):
        self.pos_x = pos_x#float
        self.pos_y = pos_y#float
        self.pos_z = pos_z#float
        self.t_caida = t_caida#float
        self.v_impac = v_impac#boolean

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
