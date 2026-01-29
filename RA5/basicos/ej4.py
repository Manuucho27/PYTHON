with open("nuevo.txt", "x") as f:
    f.write("Hola, soy un archivo nuevo.\n")

with open("nuevo.txt", "a") as f:
    while True:
        f.write(input())
        if input() == "salir":
            break
        f.write("\n")