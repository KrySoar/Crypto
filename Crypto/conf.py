import os

param = {'AutoCls':True,'Color':'red','Digest':'hex',}


def cls():
	if param["AutoCls"] == True:
		#os.system("cls") windows
		os.system("clear")
def conf(arg="list"):
	if arg == "list":
		print(param)
	elif arg == "set":
		arg = input("Parameter>")
		cls()
		if arg == 'AutoCls' or arg == 'Color':
			value = input("Parameter>Value>")
			param[arg] = value
		else:
			print("#Parameter {arg} not found,type list after conf to list the available parameters#".format(arg=arg))

	else:
		print("#Argument \"{arg}\" not found,type list after conf to list the available arguments#".format(arg=arg))


