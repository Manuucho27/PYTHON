lista= [0, 1, 2, 3, 4, 5, 6, 8, 9, 0, 1, 1, 2, 2, 2]
print("Introduce un número para ver cuantas veces está en la lista")
res=int(input("Introduce núm: "))
if lista.count(res)==1:
    print(f"El número {res} está 1 vez en la lista")
elif lista.count(res)>1:
    print(f"El número {res} está {lista.count(res)} veces en la lista")
else:
    print(f"El número {res} no está en la lista")