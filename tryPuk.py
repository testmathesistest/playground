import math

class Puk(object):
	""" Puks """
	def __init__(self, id, pos, weight, radius, velo=(0,0), color="white"):
		self.id = id #int
		self.pos = pos #(x,y) Koordinate
		self.weight = weight #float in g
		self.radius = radius #float in mm
		self.velo = velo #(x,y) vector
		self.color = color #string
		self.pulse = self.weight*math.sqrt(self.velo[0]**2+self.velo[1]**2) #float in g*mm/s

	def __eq__(self, other):
		return self.id == other.id if type(other) == Puk else False

	def __repr__(self):
		return "#"+str(self.id)

	def moveTo(self, newPos):
		""" setzt den Puk auf die Position newPos(zwei-elementiges Tupel) und aktualisiert Geschwindigkeit und Impuls """
		if type(newPos) != tuple or len(newPos) != 2:
			raise Exception("TypeError: newPos muss ein zwei-elementiges Tupel sein.")
		self.velo = (newPos[0]-self.pos[0],newPos[1]-self.pos[1])
		self.pulse = self.weight*math.sqrt(self.velo[0]**2+self.velo[1]**2)
		self.pos = newPos

	def repaint(self, newColor):
		""" setzt die Farbe des Puks auf newColor(String) """
		if type(newColor) != str:
			raise Exception("TypeError: newColor muss ein String sein.")
		self.color = newColor


class Setting(object):
	""" das "Gesamte" """
	def __init__(self, puks, size):
		self.puks = puks #list aller auf dem Tisch befindlichen Puks
		self.total = len(puks)
		self.size = size #(x,y) Breite und Höhe

	def add(self, newPuk):
		""" fügt einen Puk oder eine Liste von Puks zum Setting hinzu """
		if type(newPuk) == Puk:
			self.puks.append(newPuk)
			self.total += 1
		elif type(newPuk) == list:
			self.puks += newPuk
			self.total += len(newPuk)
		else:
			raise Exception("TypeError: "+str(type(newPuk))+" kann nicht hinzugefügt werden.")

	def remove(self, puk):
		""" entfernt einen Puk oder eine Liste von Puks aus dem Setting """
		if type(puk) != Puk:
			if type(puk) != list:
				raise Exception("TypeError: puk muss ein Puk oder eine Liste sein.")
			self.puks = list(set(self.puks)-set(puk))
			self.total -= len(puk)
		if not puk in self.puks:
			raise Exception("Error: puk ist nicht im Setting enthalten.")
		self.puks.remove(puk)
		self.total -= 1