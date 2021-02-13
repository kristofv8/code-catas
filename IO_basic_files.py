str(10)
print(type(str(10)))

myfile = open("nazwa.txt")
print(myfile.read())
myfile = open("C:\\Users\\Dell\\PycharmProjects\\pythonProject2\\venv\\Lib\\site-packages\\pip-20.3.3.dist-info\\LICENSE.txt")
print(myfile.read())
myfile.close()

with open("C:\\Users\\Dell\\PycharmProjects\\pythonProject2\\venv\\Lib\\site-packages\\pip-20.3.3.dist-info\\LICENSE.txt", mode="r") \
        as my_newfile:
    contents = my_newfile.read()
print(contents)

with open("nazwa.txt",mode="r") as nazwa:
    print(nazwa.read())
with open("nazwa.txt",mode="a") as nowy:
        nowy.write("\nThis is another line of text")
with open("nazwa.txt",mode="r") as nowy:
    print(nowy.read())