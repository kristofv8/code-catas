with open("nazwa.txt", mode="a") as nowy:
    nowy.write("\nThis is another line of text")
with open("nazwa.txt", mode="r") as nowy:
     print(nowy.read())


with open("nazwa.txt", mode="w") as nastepny:
    nastepny.write("Now should be OK")
with open("nazwa.txt", mode="r") as nastepny:
    print(nastepny.read())