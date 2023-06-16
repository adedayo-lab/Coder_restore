import os
def run(**args):
	print("[*] in directory lister") 
	files = os.listdir(".")


	return str(files)
