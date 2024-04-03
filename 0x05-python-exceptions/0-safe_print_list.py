#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	try:
		for i in my_list:
			x+=1
			print(i , end='')
		print()
		return x
	except :
		print('erreur')
