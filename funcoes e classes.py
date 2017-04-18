import random
import time

class Inspermon():
	def __init__(self, pknome, ataque, defesa, vida):
		self.a = ataque
		self.d = defesa
		self.pv = vida

	def __repr__(self):
		return "Inspermon()"

	def __str__(self):
		return self.pknome

#definindo a função que padronizará a resposta
def padroniza(resposta):
	resposta = resposta.strip(" ")
	resposta = resposta.lower()
	resposta = resposta.title()
	return resposta

#definindo a função de batalhas
def batalha(inspermon1, inspermon2, bd):
	resultado1 = [bd[inspermon2].pv]
	resultado2 = [bd[inspermon1].pv]
	for i in range (1, 1000):
		print("É o seu turno, concentre-se!")
		ação = input("Para atacar digite 'ataque', mas se você quer tentar fugir, digite 'fuja'")
		ação = padroniza(ação)	
		dano1 = bd[inspermon1].a - bd[inspermon2].d
		dano2 = bd[inspermon2].a - bd[inspermon1].d
		if ação == "Ataque":
			resultado1 = resultado1 + [resultado1[i-1] - dano1]
			resultado2 = resultado2 + [resultado2[i-1] - dano2]
			print("Seu Inspermon está atacando")
			time.sleep(2)
			if resultado1[i] > 0:
				print("Os pontos de vida de seu inimigo foram de {0} para {1}".format(resultado1[i-1], resultado1[i]))
			if resultado1[i] <= 0:
				print("Os pontos de vida de seu inimigo foram de {0} para 0".format(resultado1[i-1]))
				print("{0} desmaiou, {1} é o vencedor da batalha!".format(inspermon2, inspermon1))
				print("Continuando aventura, a vida de seu inspermon foi regenerada")
				break
			time.sleep(2)
			print("Agora seu inimigo atacará, se prepare!")
			time.sleep(2)
			print("...")
			time.sleep(1)
			if resultado2[i] > 0:
				print("Seus pontos de vida foram de {0} para {1}".format(resultado2[i-1], resultado2[i]))
			else:
				print("Seus pontos de vida foram de {0} para 0".format(resultado2[i-1]))
				print ("Seu inspermon desmaiou, que pena... Cure-o em um centro Inspermon mais proximo e tente novamente")
				break
		if ação == "Fuja":
			resultado1 = resultado1 + [resultado1[i-1]]
			resultado2 = resultado2 + [resultado2[i-1]]
			print ("OK! Vamos tentar fugir...")
			time.sleep (2)
			#criando uma probabilidade de fuga da batalha
			probD = random.randint(0, 5)
			if probD in range(0,1):
				print("Fugiu com exito!")
				break
			else:
				print ("Você não conseguiu fugir, vamos continuar a batalha!")
				pass