class Person:

    def __init__(self, num,prenom,uid, SEXE, ANNEE_NAISSANCE):
        self.num = num
        self.prenom = prenom
        self.uid = uid
        self.sexe = SEXE
        self.birthday = ANNEE_NAISSANCE
        self.min = 0
        self.max = 0
        self.median = 0

    def __str__(self):
        return self.prenom + ", " + self.sexe + ", " +\
               str(self.min) + ", " + str(self.median) + ", "+ str(self.max)
