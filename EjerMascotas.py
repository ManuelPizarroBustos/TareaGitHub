
op=1
while(op!=4):
    op=int(input("""\n**** Veterinaria Colitas Felices ****
    1. Ingresar Mascota
    2. Cantidad de Mascotas
    3. Cantidad de caracteres
    4. Salir
        Elija Opción: """))
    if(op==1):
        with open("mascotas.txt","a") as f:
            resp="S"
            while(resp=="S"):
                nom=input("\nIngrese nombre Mascota: ").capitalize()
                f.write(nom+"\n")
                resp=input("\n\tDesea agregar otra mascota S/N: ").upper()
    if(op==2):
        with open("mascotas.txt","r") as f:
            lista=f.readlines()
        print("\n\tLa cantidad de mascotas es "+str(len(lista)))
    if(op==3):
        with open("mascotas.txt","r") as f:
            lista=f.readlines()
        print(lista)
        print("Las mascotas registradas son:")
        for mas in lista:
            print(mas.strip()+" = "+str(len(mas)-1)+" caracteres")
         
    
    