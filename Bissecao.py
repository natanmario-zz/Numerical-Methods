# -*- coding: utf-8 -*-
# Função para calcular f(z)
def funcao(z):
	return z**3 + (-9*z) + 3

# Definir intervalo inicial
a = input("Digite o intervalo a: ")
b = input("Digite o intervalo b: ")


# Definir precisao e numero maximo de interações
precisao = 0.001 
maxInter = 10

Fa = funcao(a)
Fb = funcao(b)

if(Fa * Fb < 0):
	
	if(Fa == 0):
		x = a
	
	if(Fb == 0):
		x = b	

	if(abs(b-a) < precisao):
		x = a
	
	else:
			
		for i in range(1,maxInter+1):

			x = float(a+b)/2
			Fx = funcao(x)
			
			if(abs(b-a) < precisao) or (Fx == 0): 
				break
			
			if(Fa * Fx < 0):
				b = x
				
			else:
				a = x
			
			print("Interação %d" % (i))

			print("a: %f" % (a))	
			print("F(a): %f" % (Fa))

			print("b: %f" % (b))
			print("F(b): %f" % (Fb))

			print("x: %f" % (x))
			print("F(x): %f" % (Fx))
	
			print("Intervalo: %f" % (abs(b-a)))
			print("\n")


	print("Valor da raiz: %f" % (x))	

else:
	print("Intervalo mal definido")	
