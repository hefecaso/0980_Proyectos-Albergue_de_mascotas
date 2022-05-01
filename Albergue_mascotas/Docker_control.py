from os import system
import os

def menu():
    print('\n##########################')
    print('#    Control de docker   #')
    print('##########################\n')

    print('======================')
    print('Seleccione una opción')
    print('======================\n')

    print("\n1. Ver repositorios locales.")
    print("2. Ver contenedores activos y desactivados.")
    print("3. Ver último contenedor creado.")
    print("4. Borrrar contenedor con id de imágen.")
    print("5. Construir contenedor de Django.")
    print("6. Publicando contenedor de Django.")
    print("7. Salir.\n")


while True:
    menu()
    opc = input("Ingrese una opción: ")
    os.system ("clear")

    if opc == '1':
        print('=====================================')
        print("Mostrando lista de repositorios")
        system(f"sudo docker image ls")
        print('=====================================')


    elif opc == '2':
        print('====================================================================')
        print("Mostrando contenedores activos y desactivados")
        system(f"sudo docker ps -a")
        print('====================================================================')


    elif opc == '3':
        print('====================================================================')
        print("Mostrando último contenedor creado")
        system(f"sudo docker ps -l")
        print('====================================================================')


    elif opc == '4':
        print('====================================================================')
        print("Borrando contenedor con id de imágen")
        image = input("\nIngrese ID de Imágen: ")
        system(f"docker rmi {Image}")
        print('====================================================================')


    elif opc == '5':
        print('====================================================================')
        print("Construyendo contenedor de Django")
        system(f"sudo docker build --tag python-django .")
        print('====================================================================')


    elif opc == '6':
        print('====================================================================')
        print("Publicando contenedor de Django")
        system(f"sudo docker run --publish 8000:8000 python-django")
        print('====================================================================')


    else:
        break
