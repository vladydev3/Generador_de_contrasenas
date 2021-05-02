import random

print('Generador de Contraseñas')

caracteres = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ!@#$%^&*()_+,?.0123456789'

cant = int(input('\nDiga la cantidad de contraseñas a generar: '))

if cant==0:
    exit()

tamano = int(input('\nDiga la cantidad de caracteres de sus contraseñas: '))

res = input('\nQuiere eliminar algún caracter para que no aparezca en sus contraseñas? (s/n): ')

if res=='s':
    a_eliminar = input('\nDiga cuál caracter o caracteres desea eliminar de sus futuras contraseñas: ')
    
    for i in range(len(a_eliminar)):
        caracteres = caracteres.replace(a_eliminar[i],'')

print('\nAquí tiene sus contraseñas:')

for cont in range(cant):
    contrasenas = ''
    for c in range(tamano):
        contrasenas += random.choice(caracteres)
    with open('contraseñas.txt','a') as x: 
        x.write(contrasenas + '\n')
    print(contrasenas)
    print('Las contraseñas han sido guardadas en un archivo de texto llamado "contraseñas" en la dirección donde ejecutó este programa')
