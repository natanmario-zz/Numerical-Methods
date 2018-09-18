# -*- coding: utf-8 -*-

def funcao(x):
	return x**3 + (-9*x) + 3

def fi(x):
	return (x**3)/9 + 1/3

x0 = 0.5
e = 0.0005
maxIter = 10

if(abs(funcao(x0)) < e):
	raiz = x0

else:

	k = 1

	for i in range(0, maxIter):
		
		x1 = fi(x0)
		print("x1: %f" % (x1))

		if(abs(funcao(x1)) < e or abs(x1 - x0) < e):
			raiz = x1
			break
		
		x0 = x1
		k = k+1

print("Raiz é: %f" % (raiz))
