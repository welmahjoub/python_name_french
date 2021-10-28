import csv
from collections import defaultdict

from classe import Person



def readFile_prenoms():
    with open('./prenom/Liste_prenoms_Rtrail7km.csv', newline='', ) as file:
        reader = csv.reader(file, quotechar='|')
        liste = []

        for row in reader:
            p = row[0].split(';')# num,prenom,uid, SEXE, ANNEE_NAISSANCE)
            person = Person(p[0],p[1],p[2], '','')
            liste.append(person)

    return liste[3::]


def readFile_insse():
    with open('./prenom/prenoms-enfants-france.csv', newline='', ) as file:
        reader = csv.reader(file, quotechar='|')
        liste = defaultdict(list)

        for row in reader:
            p = row[0].split(';')
            prenom = p[0].lower()# num,prenom,uid, SEXE, ANNEE_NAISSANCE)
            person = Person('', prenom, '', p[1], p[2])
            tab = liste[prenom]
            tab.append(person)
            liste[prenom] = tab

    return liste



def generateOutPut(prenoms):
    with open('output/prenoms_elmahjoub_simpara.csv', 'w', newline='') as file:
        fieldnames = ['ordre', 'prenom', 'uid', 'sexe', 'age_min', 'age_median', 'age_max']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for p in prenoms:
            writer.writerow({'ordre': p.num, 'prenom': p.prenom, 'uid': p.uid, 'sexe': p.sexe,
                             'age_min': p.min, 'age_median': p.median, 'age_max': p.max})
