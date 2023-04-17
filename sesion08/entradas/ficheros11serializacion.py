"""
guargar datos en un fichero y luego recuperarlos
"""
import pickle
class Players:
    name = "jj"
    def name(self, name):
        self.name = name
         

class Status:
       score = 0
       def cantidad(self, score):
            self.score = score

class Estado:
    players = Players()
    status = Status()
    #players = 'ff'
    #status = 'f'
    life_remaning = 12
    amor = False



data = "gamestatus2.dat"
#serializacion0
f = open(data, "wb")
print("------------------------------")
e = Estado()
pickle.dump(e, f)
f.close()
print("------------------------------")

#deserializacion
f = open(data, "rb")
e1 = pickle.load(f)
f.close()
e1.players.name("armando")
print(e1.players.name)
e1.status.cantidad(10)
print(e1.status.score)
print(e1.life_remaning)
print(e1.amor)

