
def amende():
    try:
        poule = int(input('Saisir le nombre de poules tuées :' ))
        amende_poule = poule * 1
    except ValueError:
        print('Invalid input.')
        return
    try:
        chien = int(input('Saisir le nombre de chiens tués : '))
        amende_chien = chien * 3
    except ValueError:
        print('Invalid input. ')
        return
    try:
        vache = int(input('Saisir le nombre de vaches tuées : '))
        amende_vache = vache * 5
    except ValueError:
        print('Invalid input. ')
        return
    try:
        un_ami = int(input('Saisir le nombre de personnes tuées : '))
        amende_personne = un_ami * 10
    except ValueError:
        print('Invalid input. ')
        return

    amende = amende_poule + amende_chien + amende_vache + amende_personne
    nombre_point_restant= 100-amende
    
    print(f'Le montant total de l amende est de {nombre_point_restant} point.')

    cout=(nombre_point_restant// 100 )* 200
    if nombre_point_restant > 100:
        print(f'Le montant de votre permis est {cout} CFa.')
    elif nombre_point_restant < 0:
        print(f'Le montant de votre permis est {cout} CFa.')
    else :
        print("Votre permis reste valide ")



amende()





