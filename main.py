# Művelet típusok megadása
tipus = input('Milyen műveletet szeretnél elvégezni? ')



# hibakezelés
list = ['összeadás', 'kivonás', 'szorzás', 'osztás', 'hatványozás', 'mudzsuló']


# folyamat

try:
    if tipus == list[0]:
            # Számok bekérése
            szam1 = input('Mi legyen az első szám? ')
            szam2 = input('Mi legyen az második szám? ')
            result = int(szam1) + int(szam2)
            print(result)

    elif tipus == list[1]:
            # Számok bekérése
            szam1 = input('Mi legyen az első szám? ')
            szam2 = input('Mi legyen az második szám? ')
            result = int(szam1) - int(szam2)
            print(result)

    elif tipus == list[2]:
            # Számok bekérése
            szam1 = input('Mi legyen az első szám? ')
            szam2 = input('Mi legyen az második szám? ')
            result = int(szam1) * int(szam2)
            print(result)

    elif tipus == list[3]:
            # Számok bekérése
            szam1 = input('Mi legyen az első szám? ')
            szam2 = input('Mi legyen az második szám? ')
            result = int(szam1) / int(szam2)
            print(result)

    elif tipus == list[4]:
            # Számok bekérése
            szam1 = input('Mi legyen az első szám? ')
            szam2 = input('Mi legyen az második szám? ')
            result = int(szam1) ** int(szam2)
            print(result)

    elif tipus == list[5]:
            # Számok bekérése
            szam1 = input('Mi legyen az első szám? ')
            szam2 = input('Mi legyen az második szám? ')
            result = int(szam1) % int(szam2)
            print(result)

    else:
            print('Érvényes műveletet addj meg')

except ValueError:
    print('Számot adj meg!')