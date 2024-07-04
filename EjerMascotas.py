
op=1
while(op!=3):
    op=int(input("""\n**** Veterinaria Colitas Felices ****
    1. Ingresar Mascota
    2. Cantidad de Mascotas
    3. Salir
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
    
         
    
    