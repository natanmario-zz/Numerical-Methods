# -*- coding: utf-8 -*-

from sympy import symbols, diff

def funcao(x):
	return x**3 + (-9*x) + 3

def derivada(x):
	y = symbols('y')
	f = y**3 + (-9*y) + 3
	
	#Derivada de f
	df = diff(f,y)
	#Aplicação do valor na derivada
	adf = df.evalf(subs={y: x} )
	
	return adf 

x0 = 0.5 #input("Digite a aproximação inicial: ")

e = 0.0001

maxInter = 10

if(abs(funcao(x0)) < e):
	raiz = x0

else:
	k = 1
	for i in range(0, maxInter):
		x1 = x0 - (funcao(x0)/derivada(x0))
		

		print("Interação: %i" % (k))
		
		print("F(x): %f" % (funcao(x1)) )
		print("Raiz x: %f" % (x1) )

		print("\n")
	
		if(abs(funcao(x1)) < e or abs(x1 - x0) < e):
			raiz = x1
			break

		x0 = x1
		k = k + 1

print("A raiz é %f" % (raiz) )
