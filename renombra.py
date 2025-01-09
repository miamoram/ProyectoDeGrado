
import os

i = 1
path = "/home/miguel/Escritorio/dataset/verde/img/"
entradas = os.scandir(path)
for entrada in entradas:
    nombre, extension = os.path.splitext(entrada)
    des= "organic_"+str(i)+str(extension)
    print(des)
    os.rename(path+entrada.name, path+des)
    i+=1