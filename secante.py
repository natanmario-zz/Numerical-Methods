# -*- coding: utf-8 -*-
def funcao(x):
	return x**3 + (-9*x) + 3

x0 = 0.0
x1 = 1.0

e = 0.0005
maxIter = 10

if(abs(funcao(x0)) < e):
	raiz = x0

elif(abs(funcao(x1)) < e or abs(x1 - x0) < e):
	raiz = x1

else:

	k = 1
	
	for i in range(0,maxIter):
	
		x2 = x1 -  ( funcao(x1) * ( x1 - x0 ) / ( funcao(x1) - funcao(x0) ) )
		
		print("Iteração %i" % k)

		print("f(x2) = %f" % funcao(x2))
		print("x2 = %f" % x2)
		
		print("\n")
		
		if(abs(funcao(x2)) < e or abs(x2 - x1) < e ):
			
			raiz = x2
			break

		x0 = x1
		x1 = x2
		k = k + 1

print("Raiz é: %f" % raiz)
