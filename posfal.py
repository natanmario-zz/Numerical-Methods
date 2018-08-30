# -*- coding: utf-8 -*-
def funcao(z):
	return z**3 - (9*z) + 3

a = input("Digite o intervalo a: ")
b = input("Digite o intervalo b: ")

e = 0.005
iterMax = 5

Fa = funcao(a)
Fb = funcao(b)


if Fa*Fb < 0:
	
	if(Fa == 0):
		raiz = a
	if(Fb == 0):
		raiz = b
		
	if(abs(b - a) > e):
		k = 1
		
		for i in range(1,iterMax+1):
			x = ((a*Fb) - (b*Fa))/(Fb - Fa)
			Fx = funcao(x)
			
			intervalo = abs(b-a)

			print("Interação %d" % k)

			print("Valor de a: %f" % a)
			print("Fa: %f " % Fa)

			print("Valor de b: %f" % b)
			print("Fb: %f " % Fb)

			print("Valor de x: %f" % x)
			print("Fx: %f" % Fx)
			
			print("Intervalo: %f" % intervalo)

			print("\n")

			if(Fx == 0):
				raiz = x
				break
			
			if(Fa*Fx < 0):
				b = x
				Fb = Fx
			else:
				a = x
				Fa = Fx

			if(intervalo < e or abs(Fx) < e or k == iterMax):
				raiz = x
				break
			
			k = k + 1

		print("A raiz é: %f " % raiz)
	else:
		raiz = a
		print("A raiz é: %f" % raiz)			
	
else:
	print("Intervalo Inválido")
