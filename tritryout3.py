x = True
while (x):
    naam = input ('Hoe heet je?\n')
    if naam == 'stop':
        exit()
    leeftijd = input ('Hoe oud ben je?\n')
    if leeftijd == 'stop':
        exit()
    def persoonsGegevens(naam,leeftijd):
        print (f'hallo {naam} je leeftijd is {leeftijd} jaar')
    persoonsGegevens(naam,leeftijd)
