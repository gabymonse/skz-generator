import random
import time

# QUIERO QUE GENERE UN NOMBRE RANDOM (CON SU LINEA -MAKNAE O HYUNG- Y SU RACHA -3, VOCAL O DANCE) 
# Y UNA CANCION RANDOM (CON SU ALBUM Y PREGUNTANDO AL USUARIO SI LE GUSTA)
class Songs:
  def __init__(self, cadena):
    self.cadena = cadena

  def __repr__(self):
    return self.cadena

  def lists(self):
    self.go_live = ["Easy", "God's Menu", "Gone Days", "Go Live", "Pacemaker", "Phobia", "Blueprint", "Top", "Ta"]
    self.noeasy = ["Cheese", "Thunderous", 	"Domino", "Ssick", "The View", "Wolfgang", "Red Lights (Bang Chan, Hyunjin)", "Surfin' (Lee Know, Felix, Changbin)", "Gone Away (I.N, Han, Seungmin)"]

  
  def generator_song(self):
    self.go_live = ["Easy", "God's Menu", "Gone Days", "Go Live", "Pacemaker", "Phobia", "Blueprint", "Top", "Ta"]
    self.noeasy = ["Cheese", "Thunderous", 	"Domino", "Ssick", "The View", "Wolfgang", "Red Lights (Bang Chan, Hyunjin)", "Surfin' (Lee Know, Felix, Changbin)", "Gone Away (I.N, Han, Seungmin)"]
    print("Your song is...")
    self.album = random.choice(self.go_live + self.noeasy)
    print(self.album)
    if self.album in self.go_live:
        return "From the album: Go Live"
    if self.album in self.noeasy:
        return "From the album: Noeasy(Noisy)"
    
  # def does_like(self):
  #       self.like = input("do you like this song? ")
        
  #       if self.like == "yes":
  #             print("")

#----------------------------------------------------------------------------------------------
class Members:

  def __init__(self, cadena):
        self.cadena = cadena


  def __repr__(self):
    return self.cadena

  def nombres(self):
        self.name = ["Bangchan", "Lee Know", "Changbin", "hyunjin", "Han", "Felix", "Seungmin", "I.N"]

  def generator_member(self):
        self.name = ["Bangchan", "Lee Know", "Changbin", "hyunjin", "Han", "Felix", "Seungmin", "I.N"]
        print("Your random member is...")
        self.member = random.choice(self.name)
        print(self.member)
        if self.member == self.name[0]:
              return "The oldest of the group! his SKZOO is a wolf called Wolfchan =D"
        if self.member == self.name[1]:
              return "First name: Minho. his SKZOO is a Rabbit named Leebit. So Cute!"
        if self.member == self.name[2]:
              return "Part of 3RACHA! his SKZOO is a hybrid of a pig and a rabbit called Dwaekki. Adorable!"
        if self.member == self.name[3]:
              return "Part of DanceRACHA his SKZOO is a ferret named Jiniret. Go Sexy King!"
        if self.member == self.name[4]:
              return "Part of 3RACHA! his SKZOO is a quokka called Han Quokka. yes Squirrel!!"
        if self.member == self.name[5]:
              return "AKA Yongbok! his SKZOO is a chick called BbokkAri. Sunshine!!"
        if self.member == self.name[6]:
              return "Part of VocalRACHA. his SKZOO is a Puppy called PuppyM. Mong Mong!"
        if self.member == self.name[7]:
              return "Part of VocalRACHA. his SKZOO is a dessert fox called Foxl.Ny. Maknae on Top!"

#---------------------------------------------------------------------------

prueba = Songs("Welcome! this game will generate a random song from SKZ")
prueba_con_metodo = prueba.generator_song()
prueba1 = Members("Welcome! this game will generate a random member from SKZ")

print("Welcome! this game will generate a random song or member from SKZ")
print("please write 1 to generate a random song or 2 to generate a random member")
choice = input("1 or 2")
if choice == 1:
      
      print(prueba)
      print(prueba_con_metodo)

if choice == 2:
     
     print(prueba1)
     print(prueba1.generator_member()) 

# prueba = Songs("Welcome! this game will generate a random song from SKZ")
# print(prueba)
# print(prueba.generator_song())
#prueba.does_like()


# prueba1 = Members("Welcome! this game will generate a random member from SKZ")
# print(prueba1)
# print(prueba1.generator_member())