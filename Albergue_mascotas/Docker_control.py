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
    print("2. Ver contenedores activos y desactivos.")
    print("3. Ver último contenedor creado.")
    print("4. Borrrar contenedor con id de imágen.")
    print("5. Construir contenedor de Django.")
    print("6. Publicando contenedor de Django.")
    print("7. Borrrar contenedor con id de contenedor.")
    print("8. Buil con docker composer.")
    print("9. Up con docker composer.")
    print("10. Makemigrations docker-compose -> Django.")
    print("11. Migrate docker-compose -> Django.")
    print("12. Collectstatic docker-compose -> Django.")
    print("13. Ingresar a contenedor.")
    print("14. Salir.\n")


while True:
    menu()
    opc = input("Ingrese una opción: ")
    os.system ("clear")

    if opc == '1':
        print('=================================================================================')
        print("Mostrando lista de repositorios")
        print("\nsudo docker image ls\n")
        system(f"sudo docker image ls")
        print('=================================================================================')


    elif opc == '2':
        print('=================================================================================')
        print("Mostrando contenedores activos y desactivos")
        print("\nsudo docker ps -a\n")
        system(f"sudo docker ps -a")
        print('=================================================================================')


    elif opc == '3':
        print('=================================================================================')
        print("Mostrando último contenedor creado")
        print("\nsudo docker ps -l\n")
        system(f"sudo docker ps -l")
        print('=================================================================================')


    elif opc == '4':
        print('=================================================================================')
        print("Borrando contenedor con id de imágen")
        image = input("\nIngrese ID de imágen: ")
        print(f"\nsudo docker rmi -f {image}\n")
        system(f"sudo docker rmi -f {image}")
        print('=================================================================================')


    elif opc == '5':
        print('=================================================================================')
        print("Construyendo contenedor de Django\n")
        nombre = input("Ingrese el nombre para su contenedor: ")
        tag = input("Ingrese el nombre del tag: ")
        print(f'\nsudo docker build -t "{nombre}:{tag}" .\n')
        system(f'sudo docker build -t "{nombre}:{tag}" .')
        print('=================================================================================')


    elif opc == '6':
        print('=================================================================================')
        print("Publicando contenedor de Django\n")
        nombre = input("Ingrese el nombre para su contenedor: ")
        print(f"\nsudo docker run --publish 8000:8000 {nombre}\n")
        system(f"sudo docker run --publish 8000:8000 {nombre}")
        print('=================================================================================')


    elif opc == '7':
        print('=================================================================================')
        print("Borrando contenedor con id de contenedor\n")
        contenedor = input("Ingrese ID del contenedor: ")
        print(f"\nsudo docker rm -f {contenedor}\n")
        system(f"sudo docker rm -f {contenedor}")
        print('=================================================================================')


    elif opc == '8':
        print('=================================================================================')
        print("Buil con docker composer\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose up --build\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose up --build")
        print('=================================================================================')

    elif opc == '9':
        print('=================================================================================')
        print("Up con docker composer\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose up\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose up")
        print('=================================================================================')

    elif opc == '10':
        print('=================================================================================')
        print("Makemigrations docker-compose -> Django\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py makemigrations\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py makemigrations")
        print('=================================================================================')

    elif opc == '11':
        print('=================================================================================')
        print("Migrate docker-compose -> Django\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py migrate\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py migrate")
        print('=================================================================================')

    elif opc == '12':
        print('=================================================================================')
        print("Collectstatic docker-compose -> Django\n")
        print(f"\nsudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py collectstatic\n")
        system(f"sudo COMPOSE_HTTP_TIMEOUT=200 docker-compose run django_app python manage.py collectstatic")
        print('=================================================================================')

    elif opc == '13':
        print('=================================================================================')
        print("Borrando contenedor con id de contenedor\n")
        contenedor = input("Ingrese ID del contenedor: ")
        print(f"\nsudo docker exec -it {contenedor} psql -U postgres\n")
        system(f"sudo docker exec -it {contenedor} psql -U postgres")
        print('=================================================================================')


    elif opc == '14':
        print('===================')
        print("||   Saliendo.   ||")
        print('===================')
        break


    else:
        menu()
        opc = input("Ingrese una opción: ")
        os.system ("clear")
