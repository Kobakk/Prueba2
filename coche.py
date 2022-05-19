class Coche:
	rapido = False
	
	def __init__(self, color, modelo):
		self.color = color
		self.modelo = modelo
		print(f"Acaba de salir un coche {self.color} {self.modelo}. ")
		
coche_1 = Coche("negro", "Mustang")
coche_2 = Coche("blanco", "Mercedez")
