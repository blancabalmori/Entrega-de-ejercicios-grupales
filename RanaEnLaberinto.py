mapa= [
    ["X" , "I" , "X" , "X" , "X" , "X" , "X"],
    ["X" , " " , "X" , "X" , "T1" , " " , "X"],
    ["X" , " " , "T2" , "X" , " " , " " , "X"],
    ["X" , " " , " " , "X" , "B" , " " , "X"],
    ["X" , " " , " " , "X" , "T2" , " " , "X"],
    ["X" , "T1" , "B" , "X" , "X" , " " , "X"],
    ["X" , "X" , "X" , "X" , "X" , "S" , "X"],
]

x = 1
y = 1

print("Empieza en(0,0)")
print((mapa[y])[x])
i = 0

while (mapa[y])[x] != "X":
    direccion = input("Elige la dirección: ")
    
    if direccion == "S" or "W" or "A" or "D":
        print("Has seleccionado {}".format(direccion))
    
    if direccion == "S":
        x = x
        y += 1      
    elif direccion == "w":
        x = x
        y -= 1

    elif direccion == "A":
        x -= 1
        y = y 

    elif direccion == "d":
        x += 1
        y = y 


    else:
        print("Elige entre WASD")
        print("\n")

    print("Estás en la casilla ({},{})".format(x,y))
    if (mapa[y])[x] == ' ':
        print("La casilla elegida no es muro, continua")
    elif (mapa[y])[x] == 'S':
        print("¡Enhorabuena, has acabado el juego!")
        break
    elif (mapa[y])[x] =="T1":
        if(x==1  and y==5 ):
            x = 4
            y = 1
            print("Has encontrado un tunel, la rana avanza hasta la posición (4,3)")
        if(x==4 and y==1):
            x = 1
            y = 5
            print("Has encontrado un tunel, la rana avanza hasta la posición (1,4)")
        elif (mapa[y])[x] == "T2":
           if(x==2  and y==2 ):
            x = 4
            y = 4
            print("Has encontrado un tunel, la rana avanza hasta la posición (5,2)")
        if(x==4 and y==4):
            x = 2
            y = 2
            print("Has encontrado un tunel, la rana avanza hasta la posición (5,4)") 
    else:
        print("La casilla es un muro \nReinicia el programa para seguir jugando")