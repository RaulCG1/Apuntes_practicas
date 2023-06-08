

"""file1= open("C:/Users/rulas/OneDrive/Escritorio/Python/curso1/frases.txt","r")
print(file1.name)
print(file1.mode)

file1.close""""""
with open("C:/Users/rulas/OneDrive/Escritorio/Python/curso1/frases.txt","r") as file1:
    file_stuff=file1.read()
    print(file_stuff)
print(file1.close)
print(file_stuff)"""
"""
with open("C:/Users/rulas/OneDrive/Escritorio/Python/curso1/frases.txt","r") as file1:
    file_temp= file1.readlines()
    print(file_temp)
print(file1.close)
with open("C:/Users/rulas/OneDrive/Escritorio/Python/curso1/frases.txt","r") as file1:
    file_temp= file1.readline()
    print(file_temp)
    file_temp= file1.readline()
    print(file_temp)
print(file1.close)

"""
directorio="C:/Users/rulas/OneDrive/Escritorio/Python/curso1/frases.txt"
directorio1="C:/Users/rulas/OneDrive/Escritorio/Python/curso1/frasesss.txt"
with open(directorio,"r") as file1:
        i = 0
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
with open(directorio,"r") as file1:
    file_temp= file1.readlines(2)
    print(file_temp)
    file_temp= file1.readlines(5)
    print(file_temp)
    file_temp= file1.readlines(10)
    print(file_temp)
    file_temp= file1.readlines(12)
    print(file_temp)
print(file1.close)

with open(directorio1,"w") as file1:
     file1.write("agua de azucar")

frases= ["my name is\n","raul\n","paps\n"]
with open(directorio1,"w") as file1:
     for line in frases:
        file1.write(line)
with open(directorio,"r") as sss:
    with open(directorio1,"w") as file1:
        for line in sss:
            file1.write(line)