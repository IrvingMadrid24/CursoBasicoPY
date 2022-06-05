cal = input ("Introduce tu calificacion del curso: ")

cal = int (cal)

if cal >=700 and cal<=1000 :
    print("Felicidades, ya pasaste")
elif cal <700 and cal>=0:
    print("No pasaste, lo siento")
elif cal>1000 and cal<0:
    print("Tremendo mentiroso")
