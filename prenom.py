from statistics import median

from csv_utils import *

insee = readFile_insse()
prenoms = readFile_prenoms()

print(len(insee))
print(len(prenoms))


nb=0

for person in prenoms:
    listes_persons = insee[person.prenom.lower()]

    if listes_persons:

        sexes = [p.sexe for p in listes_persons if p.sexe]
        if sexes:
            nb = nb + 1
            person.sexe = sexes[0]

        birthdays = [int(p.birthday) for p in listes_persons if p.birthday]

        person.min = 2020 - max(birthdays)
        person.max = 2020 - min(birthdays)
        person.median = 2020 - median(birthdays)

prenoms = [p for p in prenoms if p.prenom]

for p in prenoms:
    print(p)

print(len(prenoms))

generateOutPut(prenoms)
