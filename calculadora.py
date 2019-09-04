import os
import time

def ApagarTela():
	if os.name == "posix":
		os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system ("cls")

def calculadora():
	print('1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão')

	opção = int(input('\nO que deseja fazer?(1/2/3/4):'))

	while opção:
		print('você insiriu um valor invalido')
 		opção = int(input('\no que deseja fazer(1/2/3/4):'))
	else:
	x = int(input('\ndigite o primeiro número:'))
	y = int(input('digite o segundo número:'))
	
	if opção == 1:
		r = x + y
		print(x, '+', y, ' = ' , r)
	if opção == 2:
		r = x - y
		print('\n%d-%d=', r)
	if opção == 3:
		r = x * y
		print('\n%d*%d=', r)
	if opção == 4:
		r = float(x / y)
		print('\n%d/%d=', r)

	res = input('Deseja fazer outra operação?\n\n\nS - Sim ou N - Não.\n')

	
	while res == 'S':
		ApagarTela()
		calculadora()
		res = input('Deseja fazer outra operação?\n1-sim\2-sair')
	else:
		exit

calculadora()