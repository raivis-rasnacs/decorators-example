# Piemērs bez dekoratora

a = 2
b = 5

def gudri_daliit(funkc):
    def paarbaude(a, b):
        print("Dalīsim", a, "ar", b)
        if b == 0:
            print("Hej! Nedrīkst dalīt!")
            return

        return funkc(a, b)
    return paarbaude

def daliit(a, b):
    print(a/b)

dekoreeta_funkc = gudri_daliit(daliit)

dekoreeta_funkc(a, b)

# Piemērs ar dekoratoru

a = 2
b = 0

def gudri_daliit(funkc):
    def paarbaude(a, b):
        print("Dalīsim", a, "ar", b)
        if b == 0:
            print("Hej! Nedrīkst dalīt!")
            return

        return funkc(a, b)
    return paarbaude

@gudri_daliit
def daliit(a, b):
    print(a/b)

daliit(a, b)