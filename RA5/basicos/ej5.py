with open("datos.txt", "a") as f:
    while True:
        f.write(input())
        if input() == "salir":
            break
        f.write("\n")